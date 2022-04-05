#projet meteo
#récupération des valeurs météoroliques en fonction de la ville

from tempfile import tempdir
import requests, json
import time

# votre clé API ici
api_key = "34f23575919a8f66017360a416c31ce7"

# URL de base
base_url = "http://api.openweathermap.org/data/2.5/weather?"

class Meteo():
    def __init__(self,api_key,debug=False,language="fr"):
        self.debug=debug
        self.language=language
        # votre clé API ici
        self.api_key=api_key
        #URL de base
        self.url = "http://api.openweathermap.org/data/2.5/weather?"
        # url de la requete
        self.urlkey = base_url + "appid=" + api_key 
        self.ville_url="&q="

    
    def actualisation_var(self,ville="",latlon=()):
        if ville:
            self.requete_ville(ville)
        elif latlon:
            self.requete_latlon(latlon[0],latlon[1])
        self.time_ascii=time.asctime()
        self.main = self.dict["main"]
        self.coord = self.dict["coord"]
        self.weather = self.dict["weather"][0]
        self.wind = self.dict["wind"]
        self.clouds = self.dict["clouds"]
        self.sys = self.dict["sys"]

        self.TKelvin=float(self.main["temp_min"])+float(self.main["temp_max"])
        self.TKelvin/=2
        self.TCelsus=self.TKelvin-273.15

        self.Hpourcent=self.main["humidity"]

        self.Pbar=self.main["pressure"]

        self.icon_weather=self.weather["icon"]
        self.description_weather=self.weather["description"]
    
    def get_url(self,url,proxy={}):
        url+="&lang={lang}".format(lang=self.language)
        if 'http' in proxy:
            return requests.get(url, proxies=proxy)
        else:
            return requests.get(url)

    def requete_latlon(self,lat,lon):  
        url=self.urlkey + "&lat={lat}&lon={lon}".format(lat=lat,lon=lon)
        response = self.get_url(url)
        self.dict = response.json()
        if self.debug:
            print(url)
            print(self.dict)
    
    def requete_ville(self,ville):  
        url=self.urlkey + self.ville_url + ville
        response = self.get_url(url)
        self.dict = response.json()
        if self.debug:
            print(url)
            print(self.dict)
    

if __name__=="__main__":
    m=Meteo(api_key)
    m.actualisation_var("Le Mans")
    meteo=(m.Pbar,m.TCelsus,m.Hpourcent)  #exécute la fonction gérant la requête GET
    print("affichage du tuple", meteo) # affiche les 3 valeurs sous forme de tuple
    print("pression",meteo[0]) # affiche la pression
    print("temperature",meteo[1]) # affiche la température
    print("humidite",meteo[2]) # affiche l'humidité
