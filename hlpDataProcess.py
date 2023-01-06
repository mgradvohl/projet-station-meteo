#-----------------------------------------------------------------------------------------------------------------------
# Weather Station Project - hlpDataProcess - Helper providing physical data from electrical measures            JYC-2022
#-----------------------------------------------------------------------------------------------------------------------

from Station_share import EMes, PMes

class PhysicalConversions:
    def ConvertToPhysical(self):
        #
        # ===ToDo===
        #
        PMes.Direction    = 0   # convert EMes.Girouette    Voltage  to integer position    (0 to 7)
        PMes.Station      = 0   # convert EMes.Encodeur     GrayCode to integer position    (0 to 15)
        PMes.Humidite     = 0   # convert EMes.Humidimetre  25Hz : 100% / 100Hz : 0%        (constraint in the range 0-100)
        PMes.Temperature  = 0   # convert EMes.Thermometre  °C = (Vcapteur x 100) - 273,15
        PMes.Luminosite   = 0   # convert EMes.Luxmetre     4,8V : 0 lux / 0V : 150000 lux  (constraint in the range 0-150000)
        PMes.Pluviometrie = 0   # convert EMes.Pluviometre  1 imp. = 0,2794mm
        PMes.Vitesse      = 0   # convert EMes.Anemometre   1 imp./s = 2,4km/h
