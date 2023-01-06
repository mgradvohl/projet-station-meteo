#-----------------------------------------------------------------------------------------------------------------------
# Weather Station Project - hlpDataMeasure - Helper providing data from sensors measuring                       JYC-2022
#-----------------------------------------------------------------------------------------------------------------------
# Sensors :
# --------------------
# Humidity     AI2
# Wind Vane    AI3
# Temperature  AI6
# Brightness   AI7
# Rain Gauge   P0.7
# Encoder      P1.0..3
# Anemometer   PFI0
#-----------------------------------------------------------------------------------------------------------------------

import nidaqmx
import nidaqmx.system
from nidaqmx.task import Task

from Station_share import EMes, ErMes

class DataMeasure:
    wTask : Task = None
    bTask : Task = None
    nTask : Task = None
    cTask : Task = None

    NbSamples    = 200
    RateTiming   = 5000
    SampleTime   = 1 / RateTiming
    PrevPluv     = True

    #-------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        EMes.HumidimetreAX = [0.0] * self.NbSamples
        EMes.HumidimetreAY = [0.0] * self.NbSamples
        for i in range(0, len(EMes.HumidimetreAX)): EMes.HumidimetreAX[i] = (self.SampleTime * i) * 1000

    #-------------------------------------------------------------------------------------------------------------------
    def RegError(self, e : nidaqmx.DaqError):
        import inspect

        ErMes.CurrentCode = e.error_code

        if ErMes.ErrorFlag: return

        ErMes.ErrorFlag         = True
        ErMes.ErrorFunctionName = __name__+"\\"+inspect.currentframe().f_back.f_code.co_name    # get caller function name
        ErMes.ErrorCode         = e.error_code
        ErMes.ErrorType         = e.error_type
        ErMes.ErrorMessage      = e.__str__().replace('\n', '  ')
        
    #-------------------------------------------------------------------------------------------------------------------
    def ClearError(self):
        ErMes.CurrentCode       = 0
        ErMes.ErrorFlag         = False
        ErMes.ErrorFunctionName = ""
        ErMes.ErrorCode         = 0
        ErMes.ErrorType         = ""
        ErMes.ErrorMessage      = ""

    #-------------------------------------------------------------------------------------------------------------------
    def Open(self):
        from nidaqmx.constants import TerminalConfiguration, AcquisitionType, LineGrouping, Edge

        try:
            #...........................................................................................................
            DevName = ""
            for device in nidaqmx.system.System.local().devices:
                if device.product_type.find("USB-600") != -1:
                    DevName = device.name
                    break
            if DevName == "": raise(nidaqmx.DaqError("Device auto-search failed", -200220, "No task"))
            #...........................................................................................................
            self.wTask = nidaqmx.Task                      ("WaveformTask")
            self.wTask.ai_channels.add_ai_voltage_chan     (physical_channel = DevName+"/ai2:3, "+DevName+"/ai6:7", terminal_config = TerminalConfiguration.RSE)
            self.wTask.timing.cfg_samp_clk_timing          (rate= self.RateTiming, sample_mode = AcquisitionType.FINITE, samps_per_chan = self.NbSamples)
            #...........................................................................................................
            self.bTask = nidaqmx.Task                      ("BitTask")
            self.bTask.di_channels.add_di_chan             (lines = DevName+"/port0/line7", line_grouping = LineGrouping.CHAN_PER_LINE)
            #...........................................................................................................
            self.nTask = nidaqmx.Task                      ("iNtegerTask")
            self.nTask.di_channels.add_di_chan             (lines = "Dev4/port1/line0:3", line_grouping = LineGrouping.CHAN_FOR_ALL_LINES)
            #...........................................................................................................
            self.cTask = nidaqmx.Task                      ("CounterTask")
            self.cTask.ci_channels.add_ci_count_edges_chan (counter = DevName+"/ctr0", edge = Edge.FALLING).ci_count_edges_term = "/"+DevName+"/pfi0"
            self.cTask.start()
            #...........................................................................................................
            ErMes.CurrentCode = 0
        except nidaqmx.DaqError as e:
            self.RegError(e)

    #-------------------------------------------------------------------------------------------------------------------
    def FastRead(self):
        from statistics import mean

        try:
            #...........................................................................................................
            if self.wTask == None: raise(nidaqmx.DaqError("Task doesn't exist", -200088, "WaveformTask"))
            
            Samples = self.wTask.read(number_of_samples_per_channel=self.NbSamples)
            self.wTask.wait_until_done()
            
            ew = self.GetEdgesWidth(trigger=2, data=Samples[0])
            if ew > 0: EMes.Humidimetre = self.RateTiming / ew

            EMes.HumidimetreAY = Samples[0]
            
            EMes.Girouette   = mean(Samples[1])
            EMes.Thermometre = mean(Samples[2])
            EMes.Luxmetre    = mean(Samples[3])

            #...........................................................................................................
            if self.bTask == None: raise(nidaqmx.DaqError("Task doesn't exist", -200088, "BitTask"))

            b = self.bTask.read()
            self.bTask.wait_until_done()

            if (self.PrevPluv and (not b)) : EMes.Pluviometre += 1  # +1 if falling edge (1 --> 0)
            self.PrevPluv = b

            #...........................................................................................................
            if self.nTask == None: raise(nidaqmx.DaqError("Task doesn't exist", -200088, "iNtegerTask"))

            EMes.Encodeur = self.nTask.read()
            self.nTask.wait_until_done()
            #...........................................................................................................
            ErMes.CurrentCode = 0
        except nidaqmx.DaqError as e:
            self.RegError(e)

    #-------------------------------------------------------------------------------------------------------------------
    def SlowRead(self):
        try:
            if self.cTask == None: raise(nidaqmx.DaqError("Task doesn't exist", -200088, "CounterTask"))

            EMes.Anemometre = self.cTask.read()
            self.cTask.wait_until_done()
            self.cTask.stop()
            self.cTask.start()

            ErMes.CurrentCode = 0
        except nidaqmx.DaqError as e:
            self.RegError(e)
        
    #-------------------------------------------------------------------------------------------------------------------
    def Close(self):
        try:
            if self.wTask != None: self.wTask.close()
            if self.bTask != None: self.bTask.close()
            if self.nTask != None: self.nTask.close()
            if self.cTask != None: self.cTask.close()

            self.wTask = None
            self.bTask = None
            self.nTask = None
            self.cTask = None

            ErMes.CurrentCode = 0
        except nidaqmx.DaqError as e:
            self.RegError(e)

    #-------------------------------------------------------------------------------------------------------------------
    def GetEdgesWidth(self, trigger, data):
        # def GetPeriod(Tab):
            # Period = 100 #replace with period compute
            # Begin = 10 #replace with begin compute
            # return Period, Begin

        for i in range(0, len(data)):
            if data[i] < trigger : break       # finding low state
        if i == len(data)-1 : return -1        # -1  if not found

        j = i
        for i in range(j, len(data)):
            if data[i] > trigger : break       # finding first rising edge
        if i == len(data)-1 : return -1        # -1  if not found
        FirstEdge = i

        j = i
        for i in range(j, len(data)):
            if data[i] < trigger : break       # finding low state
        if i == len(data)-1 : return -1        # -1  if not found

        j = i
        for i in range(j, len(data)):
            if data[i] > trigger : break       # finding second rising edge
        if i == len(data)-1 : return -1        # -1  if not found
        SecondEdge = i

        Period = SecondEdge - FirstEdge

        return Period
