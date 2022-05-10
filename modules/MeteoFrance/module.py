import webbrowser
from meteofrance_api import MeteoFranceClient
import datetime


class MeteoUtilities:
    def print_forecast(self, forecast):
        dt = datetime.datetime.fromtimestamp(forecast["dt"])
        sun_rise = datetime.datetime.fromtimestamp(forecast["sun"]["rise"])
        sun_set = datetime.datetime.fromtimestamp(forecast["sun"]["set"])
        print(f"[Meteo] Information pour le {dt.strftime('%d/%m/%Y à %H:%M')} :")
        print(f"        - Température : Min {forecast['T']['min']}°C - Max {forecast['T']['max']}°C")
        print(f"        - Humidité : Min {forecast['humidity']['min']}% - Max {forecast['humidity']['max']}%")
        print(f"        - Précipitations : {forecast['precipitation']['24h']}mm")
        print(f"        - Soleil : Levé à {sun_rise.strftime('%H:%M')} - Couché à {sun_set.strftime('%H:%M')} - UV : {forecast['uv'] or 'Inconnu'}")
        print(f"        - Appréciation : {forecast['weather12H']['desc']}")

class MeteoFrance:
    client = MeteoFranceClient()
    utilities = MeteoUtilities()
    
    def info(self, zolo, module, args):
        """
        Info about MeteoFrance module

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        print(f"[Meteo] Version {module.version}")
        
    def picture(self, zolo, module, args):
        """
        Get Picture of the Day

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        potd = MeteoFrance.client.get_picture_of_the_day()
        print(f"[Meteo] Description PotD : {potd.description}")
        rep = input("[Meteo] Ouvrir l'image ? (y/n) : ")
        if rep == "y":
            webbrowser.open(potd.image_hd_url)
        
        
    def weekly(self, zolo, module, args):
        """
        Get weekly information about city

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        place = MeteoFrance.client.search_places(" ".join(args))[0]
        forecast = MeteoFrance.client.get_forecast_for_place(place)
        
        for i in forecast.daily_forecast:
            MeteoFrance.utilities.print_forecast(i)
            
    def daily(self, zolo, module, args):
        """
        Get daily information about city

        Args:
            zolo (Zolo): Zolo
            module (Module): Current Module
            args (list(string)): List of arguments of command
        """
        place = MeteoFrance.client.search_places(" ".join(args))[0]
        forecast = MeteoFrance.client.get_forecast_for_place(place)
        MeteoFrance.utilities.print_forecast(forecast.today_forecast)
