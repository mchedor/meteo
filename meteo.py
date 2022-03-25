#projet meteo
#récupération des valeurs météoroliques en fonction de la ville

from tempfile import tempdir
import requests, json

# votre clé API ici
api_key = "34f23575919a8f66017360a416c31ce7"

# URL de base
base_url = "http://api.openweathermap.org/data/2.5/weather?"

class Meteo():
    def __init__(self,api_key):
        # votre clé API ici
        self.api_key=api_key
        #URL de base
        self.ville_url = "http://api.openweathermap.org/data/2.5/weather?"
        # url de la requete
        self.urlkey = base_url + "appid=" + api_key + "&q="
    
    def actualisation_var(self,ville):
        self.requete_ville(ville)
        self.main = self.dict["main"]
        self.coord = self.dict["coord"]
        self.weather = self.dict["weather"]
        self.wind = self.dict["wind"]
        self.clouds = self.dict["clouds"]
        self.sys = self.dict["sys"]

        self.TKelvin=float(self.main["temp_min"])+float(self.main["temp_max"])
        self.TKelvin/=2
        self.TCelsus=self.TKelvin-273.15

        self.Hpourcent=self.main["humidity"]

        self.Pbar=self.main["pressure"]
        

    
    def requete_ville(self,ville):  
        url=self.ville_url + "appid=" + self.api_key + "&q=" + ville
        response = requests.get(url)
        self.dict = response.json()
    

if __name__=="__main__":
    m=Meteo(api_key)
    m.actualisation_var("Le Mans")
    meteo=(m.Pbar,m.TCelsus,m.Hpourcent)  #exécute la fonction gérant la requête GET
    print("affichage du tuple", meteo) # affiche les 3 valeurs sous forme de tuple
    print("pression",meteo[0]) # affiche la pression
    print("temperature",meteo[1]) # affiche la température
    print("humidite",meteo[2]) # affiche l'humidité
