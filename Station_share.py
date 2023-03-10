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

    # pour les valeurs min
    VitesseMin     : float = 30
    TemperatureMin : float = 50
    LuminositeMin  : float = 150
    HumiditeMin    : float = 100
    PluviometrieMin: float = 10

    # pour les valeurs max
    VitesseMax     : float = 0
    TemperatureMax : float = 0
    LuminositeMax  : float = 0
    HumiditeMax    : float = 0
    PluviometrieMax: float = 0

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
from hlpDataFile import DataFileHelper
import matplotlib.colors as mcolors

GraphHumidite  : GraphPlot = None
ChartGirouette : ChartPlot = None
PeakVitesse    : PeakPlot  = None
PeakHistory    : DataFileHelper = None

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

# ===Done=== 
# definition of function clamp to update progress bars 
def clamp(num, min_value, max_value):
    num = max(min(num, max_value), min_value)
    return num

def GUIUpdate(root, w):
    import time
    from datetime import datetime
    
    global GraphHumidite, ChartGirouette, PeakVitesse, PeakHistory

    # create three graphs on GUI at the first call
    if GraphHumidite  == None: GraphHumidite  = GraphPlot(root, w.EGraphHumidite)
    if ChartGirouette == None: ChartGirouette = ChartPlot(root, w.EChartGirouette,  100)
    if PeakVitesse    == None: PeakVitesse    = PeakPlot (root, w.PChartBourrasques,100)
    if PeakHistory    == None: PeakHistory    = DataFileHelper("historique.txt")
    
    # ===Done===  fullfill PeakPlot class in hlpGUIGraph.py and create PChartBourrasques canvas on GUI
    #
    #if PeakVitesse    == None: PeakVitesse    = PeakPlot (root, w.PChartBourrasques,    100)
    
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
    # ===Done=== copy physical measures to indicators
    #
    w.PDirecVent   ["text"]  = "{:s}"       .format(PMes.Direction)
    w.PVitVent     ["text"]  = "{:.1f} km/h".format(PMes.Vitesse)
    w.PTemperature ["text"]  = "{:.1f} ??C"  .format(PMes.Temperature)
    w.PLuminosite  ["text"]  = "{:.0f} kLux".format(PMes.Luminosite)
    w.PHumidite    ["text"]  = "{:.0f} %"   .format(PMes.Humidite)
    w.PPluviometrie["text"]  = "{:.0f} mm"  .format(PMes.Pluviometrie)
    w.PNombreStation["text"] = "{:.0f} "    .format(PMes.Station)
    #
    # create the "clamp" function to constraint data into limits
    #
    w.PBVitVent      ["value"] = clamp(int(PMes.Vitesse),      0, 30)
    w.PBTemperature  ["value"] = clamp(int(PMes.Temperature),  0, 50)
    w.PBLuminosite   ["value"] = clamp(int(PMes.Luminosite),   0, 150)
    w.PBHumidite     ["value"] = clamp(int(PMes.Humidite),     0, 100)
    w.PBPluviometrie ["value"] = clamp(int(PMes.Pluviometrie), 0, 10)
    #
    #
    # ===Done=== : - update Label PListeVitesse with peak_list
    #              - save peak_list in text file # peakHistory.saveHistory(peak_list)

    peak_list = PeakVitesse.Plot(datetime.now().strftime('%d/%m/%Y %H:%M:%S'), PMes.Vitesse, PMes.Direction)

    w.PTexteBourrasques ["text"] += peak_list
    PeakHistory.saveHistory(peak_list)

    # update status message
    if not ErMes.ErrorFlag:
        w.Etat       ['text'] = "Mesures en cours ..."
    else:
        w.Etat       ['text'] = "Function: {:s}  Code: {:d}  Type: {:d}".format(ErMes.ErrorFunctionName, ErMes.ErrorCode, ErMes.ErrorType)

def MinMaxUpdate(w2):
    # ===Done===
    # show min and max values on second window
    w2.MinVitVent     ["text"]  = "{:.1f} km/h".format(PMes.VitesseMin)
    w2.MinTemperature ["text"]  = "{:.1f} ??C"  .format(PMes.TemperatureMin)
    w2.MinLuminosite  ["text"]  = "{:.1f} kLux".format(PMes.LuminositeMin)
    w2.MinHumidite    ["text"]  = "{:.1f} %"   .format(PMes.HumiditeMin)
    w2.MinPluviometrie["text"]  = "{:.1f} mm"  .format(PMes.PluviometrieMin)
    
    w2.MaxVitVent     ["text"]  = "{:.1f} km/h".format(PMes.VitesseMax)
    w2.MaxTemperature ["text"]  = "{:.1f} ??C"  .format(PMes.TemperatureMax)
    w2.MaxLuminosite  ["text"]  = "{:.1f} kLux".format(PMes.LuminositeMax)
    w2.MaxHumidite    ["text"]  = "{:.1f} %"   .format(PMes.HumiditeMax)
    w2.MaxPluviometrie["text"]  = "{:.1f} mm"  .format(PMes.PluviometrieMax)