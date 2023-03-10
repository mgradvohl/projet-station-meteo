#-----------------------------------------------------------------------------------------------------------------------
# Weather Station Project - Main - Program launcher, Timed loops manager, Perf. monitoring                      JYC-2022
# 
# Binome
# Marina BRASIL GRADVOHL
# Mouhamed GUEYE
# 
#-----------------------------------------------------------------------------------------------------------------------

from Station_share import GUIStart, EMes, ErMes

#-- Timed Loops functions ----------------------------------------------------------------------------------------------
import time
import continuous_threading
from hlpDataMeasure import DataMeasure
from hlpDataProcess import PhysicalConversions

TimedLoopFastPeriod = 0.1  # time in seconds
TimedLoopSlowPeriod = 1    # time in seconds
#.......................................................................................................................
def TimedLoopsStart():
    global dm, pc, tf, ts, fcode, scode
    global PrevLoopFTime, PrevLoopSTime

    dm = DataMeasure()
    dm.Open()
    pc = PhysicalConversions()
    PrevLoopFTime = PrevLoopSTime = time.perf_counter()
    fcode = scode = 0

    tf = continuous_threading.PeriodicThread(TimedLoopFastPeriod, TimedLoopFast)
    ts = continuous_threading.PeriodicThread(TimedLoopSlowPeriod, TimedLoopSlow)

    tf.start()
    ts.start()
#.......................................................................................................................
def TimedLoopFast():
    global dm, pc, PrevLoopFTime, fcode

    t0 = time.perf_counter()

    EMes.TempsBoucleR = (t0 - PrevLoopFTime) * 1000   # time in milliseconds
    PrevLoopFTime     = t0

    dm.FastRead()
    fcode = ErMes.CurrentCode

    if (fcode == 0) and (scode == 0): dm.ClearError()
    pc.ConvertToPhysical()
    pc.mesuresMinMax()

    EMes.DureeMesures = (time.perf_counter()-t0) * 1000   # time in milliseconds

#.......................................................................................................................
def TimedLoopSlow():
    global dm, PrevLoopSTime, scode

    t0 = time.perf_counter()

    EMes.TempsBoucleL = (t0 - PrevLoopSTime) * 1000   # milliseconds
    PrevLoopSTime     = t0

    dm.SlowRead()
    scode = ErMes.CurrentCode
#.......................................................................................................................
def TimedLoopsStop():
    global tf, ts, dm

    tf.join()
    ts.join()
    dm.Close()

#-- Application start & stop -------------------------------------------------------------------------------------------
if __name__ == "__main__":
    import os; os.system('cls')
    TimedLoopsStart() 
    GUIStart()
    TimedLoopsStop()
    

#-----------------------------------------------------------------------------------------------------------------------
