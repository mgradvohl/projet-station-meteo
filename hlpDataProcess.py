#-----------------------------------------------------------------------------------------------------------------------
# Weather Station Project - hlpDataProcess - Helper providing physical data from electrical measures            JYC-2022
#-----------------------------------------------------------------------------------------------------------------------

from Station_share import EMes, PMes, conversion

class PhysicalConversions:
    def ConvertToPhysical(self):
        #
        # ===Done===
        # data treatment to convert from electrical to physical measurements

        # function to convert tension values measured in the Girrouette 
        # and convert according to the designated cardinal points

        def convGirrouette(ValeurGirouette):
            direction = ""
            if ((ValeurGirouette <= 3.8 and ValeurGirouette >= 3.7) 
                or (ValeurGirouette <= 2.0 and ValeurGirouette >= 1.9)):
                direction = "NORD"
            elif ((ValeurGirouette <= 1.5 and ValeurGirouette >= 1.4)
                or (ValeurGirouette <= 1.3 and ValeurGirouette >= 1.2)):
                direction = "SUD"
            elif ((ValeurGirouette <= 4.5 and ValeurGirouette >= 4.4)
                or (ValeurGirouette <= 4.0 and ValeurGirouette >= 3.9)):
                direction = "OUEST"
            elif ValeurGirouette <= 0.5 and ValeurGirouette >= 0.3:
                direction = "EST"
            elif ((ValeurGirouette <= 4.3 and ValeurGirouette >= 4.2)
                or (ValeurGirouette <= 3.4 and ValeurGirouette >= 3.3)):
                direction = "NORD OUEST"
            elif ValeurGirouette <= 2.3 and ValeurGirouette >= 2.2:
                direction = "NORD EST"
            elif ((ValeurGirouette <= 1 and ValeurGirouette >= 0.9)
                or (ValeurGirouette <= 0.7 and ValeurGirouette >= 0.6)):
                direction = "SUD EST"
            elif ((ValeurGirouette <= 3.1 and ValeurGirouette >= 3.0)
                or (ValeurGirouette <= 2.9 and ValeurGirouette >= 2.8)):
                direction = "SUD OUEST"
            
            return direction

        PMes.Direction    = convGirrouette(EMes.Girouette)      # convert EMes.Girouette    Voltage  to integer position    (0 to 7)
        PMes.Station      = conversion(EMes.Encodeur)           # convert EMes.Encodeur     GrayCode to integer position    (0 to 15)
        PMes.Humidite     = -70/89 * EMes.Humidimetre + 119.66  # convert EMes.Humidimetre  25Hz : 100% / 100Hz : 0%        (constraint in the range 0-100)
        PMes.Temperature  = ((EMes.Thermometre - 3)/0.01) + 25  # convert EMes.Thermometre  with the 3V <-> 25°C reference
        PMes.Luminosite   = -31.25 * EMes.Luxmetre + 150        # convert EMes.Luxmetre     4,8V : 0 lux / 0V : 150000 lux  (constraint in the range 0-150000)
        PMes.Pluviometrie = EMes.Pluviometre * 0.2794           # convert EMes.Pluviometre  1 imp. = 0,2794mm
        PMes.Vitesse      = EMes.Anemometre * 2.4               # convert EMes.Anemometre   1 imp./s = 2,4km/h

    def mesuresMinMax(self):

        # valeurs minimales
        if PMes.Vitesse < PMes.VitesseMin:
            PMes.VitesseMin = PMes.Vitesse
        if PMes.Temperature < PMes.TemperatureMin:
            PMes.TemperatureMin = PMes.Temperature
        if PMes.Luminosite < PMes.LuminositeMin:
            PMes.LuminositeMin = PMes.Luminosite
        if PMes.Humidite < PMes.HumiditeMin:
            PMes.HumiditeMin = PMes.Humidite
        if PMes.Pluviometrie < PMes.PluviometrieMin:
            PMes.PluviometrieMin = PMes.Pluviometrie

        # valeurs maximales
        if PMes.Vitesse > PMes.VitesseMax:
            PMes.VitesseMax = PMes.Vitesse
        if PMes.Temperature > PMes.TemperatureMax:
            PMes.TemperatureMax = PMes.Temperature
        if PMes.Luminosite > PMes.LuminositeMax:
            PMes.LuminositeMax = PMes.Luminosite
        if PMes.Humidite > PMes.HumiditeMax:
            PMes.HumiditeMax = PMes.Humidite
        if PMes.Pluviometrie > PMes.PluviometrieMax:
            PMes.PluviometrieMax = PMes.Pluviometrie
        
