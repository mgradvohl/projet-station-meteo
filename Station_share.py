#-----------------------------------------------------------------------------------------------------------------------
# Weather Station Project - Share - Variables & Functions shared with Model, View, Controller                   JYC-2022
#-----------------------------------------------------------------------------------------------------------------------

#-- Global variables ---------------------------------------------------------------------------------------------------
class ElectricalMeasures:
    Humidimetre   : float = 0
    HumidimetreAX : float = []
    HumidimetreAY : float = []
    Girouette     : float = 0
    Thermometre   : float = 0
    Luxmetre      : float = 0
    Pluviometre   : int   = 0
    Encodeur      : int   = 0
    Anemometre    : int   = 0
    DureeMesures  : int   = 0
    TempsBoucleR  : int   = 0
    TempsBoucleL  : int   = 0

class PhysicalMeasures:
    Direction    : int   = 0
    Vitesse      : float = 0
    Temperature  : float = 0
    Luminosite   : float = 0
    Humidite     : float = 0
    Pluviometrie : float = 0
    Station      : int   = 0

class ErrorMeasures:
    CurrentCode       : int  = 0
    ErrorFlag         : bool = False
    ErrorFunctionName : str  = ""
    ErrorCode         : int  = 0
    ErrorType         : str  = ""
    ErrorMessage      : str  = ""

EMes  = ElectricalMeasures()
PMes  = PhysicalMeasures()
ErMes = ErrorMeasures()


#-- GUI manage ---------------------------------------------------------------------------------------------------------
def GUIStart():
    import Station_support
    Station_support.main()
#.......................................................................................................................
def GUICenter(win):
    win.update_idletasks()

    width        = win.winfo_width()
    frm_width    = win.winfo_rootx() - win.winfo_x()
    win_width    = width + 2 * frm_width
    height       = win.winfo_height()
    title_height = win.winfo_rooty() - win.winfo_y()
    win_height   = height + title_height + frm_width

    x = win.winfo_screenwidth()  // 2 - win_width  // 2
    y = win.winfo_screenheight() // 2 - win_height // 2

    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()
#.......................................................................................................................
from hlpGUIGraph import ChartPlot, GraphPlot, PeakPlot
import matplotlib.colors as mcolors

GraphHumidite  : GraphPlot = None
ChartGirouette : ChartPlot = None
PeakVitesse    : PeakPlot  = None

# ===Done=== 
# function to convert the numbers read by the 
# encoder and the values written in the board
def conversion(bits):
    if bits == 15:
        return 0
    elif bits == 14:
        return 1
    elif bits == 10:
        return 2
    elif bits == 11:
        return 3
    elif bits == 9:
        return 4
    elif bits == 8:
        return 5
    elif bits == 12:
        return 6
    elif bits == 13:
        return 7
    elif bits == 5:
        return 8
    elif bits == 4:
        return 9    
    elif bits == 0:
        return 10
    elif bits == 1:
        return 11
    elif bits == 3:
        return 12
    elif bits == 2:
        return 13
    elif bits == 6:
        return 14
    elif bits == 7:
        return 15

def GUIUpdate(root, w):
    global GraphHumidite, ChartGirouette
    
    # create three graphs on GUI at the first call
    if GraphHumidite  == None: GraphHumidite  = GraphPlot(root, w.EGraphHumidite)
    if ChartGirouette == None: ChartGirouette = ChartPlot(root, w.EChartGirouette, 100)
   #if PeakVitesse    == None: PeakVitesse    = PeakPlot (root, w.PPeakVitesse,    100)  ===ToDo===
    
    # ===ToDo===  fullfill PeakPlot class in hlpGUIGraph.py and create PPeakVitesse canvas on GUI
    #
    #if PeakVitesse    == None: PeakVitesse    = PeakPlot (root, w.PPeakVitesse,    100)
    
    # update electrical measures
    w.EHumidimetre  ["text"]  = "{:.0f} Hz".format(EMes.Humidimetre)
    w.EGirouette    ["text"]  = "{:.3f} V" .format(EMes.Girouette)
    w.EThermometre  ["text"]  = "{:.3f} V" .format(EMes.Thermometre)
    w.ELuxmetre     ["text"]  = "{:.3f} V" .format(EMes.Luxmetre)
    w.EPluviometre  ["text"]  = "{:.0f}"   .format(EMes.Pluviometre)
    w.EEncodeur     ["text"]  = "{:.0f}"   .format(conversion(EMes.Encodeur))
    w.EAnemometre   ["text"]  = "{:.0f}"   .format(EMes.Anemometre)
    w.EDureeMesures ["text"]  = "{:.0f} ms".format(EMes.DureeMesures)
    w.ETempsBoucleR ["text"]  = "{:.0f} ms".format(EMes.TempsBoucleR)
    w.ETempsBoucleL ["text"]  = "{:.0f} ms".format(EMes.TempsBoucleL)

    # ===Done=== 
    # update physical measures
    w.PDirecVent   ["text"]  = "{:s}"       .format(PMes.Direction)
    w.PVitVent     ["text"]  = "{:.1f} km/h".format(PMes.Vitesse)
    w.PTemperature ["text"]  = "{:.1f} °C"  .format(PMes.Temperature)
    w.PLuminosite  ["text"]  = "{:.0f} kLux".format(PMes.Luminosite)
    w.PHumidite    ["text"]  = "{:.0f} %"   .format(PMes.Humidite)
    w.PPluviometrie["text"]  = "{:.0f} mm"  .format(PMes.Pluviometrie)
    w.PNombreStation["text"] = "{:.0f} "    .format(PMes.Station)

    # ===Done=== set Encodeur boolean indicators (background color value : light if bit true, dark else)
    # For each bit read by the encoder and converted, we make a binary comparison 
    # and show the color grey (f0ffff) if true and yellow (abc) if false
    w.EP1_0["bg"] = '#f0ffff' if (conversion(EMes.Encodeur) & 0b00000001) == 0b00000001  else '#abc'               # use this model   : x = ValTrue  if (condition)  else ValFalse
    w.EP1_1["bg"] = '#f0ffff' if (conversion(EMes.Encodeur) & 0b00000010) == 0b00000010  else '#abc'
    w.EP1_2["bg"] = '#f0ffff' if (conversion(EMes.Encodeur) & 0b00000100) == 0b00000100  else '#abc'               # use named colors : https://matplotlib.org/stable/gallery/color/named_colors.html
    w.EP1_3["bg"] = '#f0ffff' if (conversion(EMes.Encodeur) & 0b00001000) == 0b00001000  else '#abc'

    GraphHumidite.Plot (EMes.HumidimetreAX, EMes.HumidimetreAY)
    ChartGirouette.Plot(EMes.Girouette)
    
    # update physical measures
    #
    # ===ToDo=== copy physical measures to indicators
    #
    # w.PDirection    ["text"]  =      use "format" function as electrical measures
    # w.PVitesse      ["text"]  =
    # w.PTemperature  ["text"]  =      
    # w.PHumidite     ["text"]  =
    # w.PLuminosite   ["text"]  =
    # w.PPluviometrie ["text"]  =
    # w.PStation      ["text"]  =
    #
    # create the "clamp" function to constraint data into limits
    #
    # w.PBVitesse      ["value"] = clamp(int(PMes.Vitesse),      0, 30)
    # w.PBTemperature  ["value"] = clamp(int(PMes.Temperature),  0, 50)
    # w.PBLuminosite   ["value"] = clamp(int(Luminosite),        0, 150)
    # w.PBHumidite     ["value"] = clamp(int(PMes.Humidite),     0, 100)
    # w.PBPluviometrie ["value"] = clamp(int(PMes.Pluviometrie), 0, 10)
    #
    # peak_list = PeakVitesse.Plot(datetime.now(), PMes.Vitesse, PMes.Direction)
    #
    # ===ToDo=== : - update Label PListeVitesse with peak_list
    #              - save peak_list in text file

    # update status message
    if not ErMes.ErrorFlag:
        w.Etat       ['text'] = "Mesures en cours ..."
    else:
        w.Etat       ['text'] = "Function: {:s}  Code: {:d}  Type: {:d}".format(ErMes.ErrorFunctionName, ErMes.ErrorCode, ErMes.ErrorType)
