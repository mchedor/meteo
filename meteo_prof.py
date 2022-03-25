#projet meteo
#récupération des valeurs météoroliques en fonction de la ville

import requests, json

# votre clé API ici
api_key = "34f23575919a8f66017360a416c31ce7"

# URL de base
base_url = "http://api.openweathermap.org/data/2.5/weather?"


def recupereMeteo(ville):
    # url de la requete
    url = base_url + "appid=" + api_key + "&q=" + ville
    print("l'url est",url)
    print("--------------------------------------------------")
    # methode get de la requete sur le site openweathermap
    response = requests.get(url)
    # response qui va être convertit en dictionnaire
    dict = response.json()
    print("données completes",dict)
    print()
    print(dict.keys())
    print("--------------------------------------------------")
    # récupère la clé main
    main = dict["main"]
    print("données de la clé main",main)
    print("--------------------------------------------------")
    #A compléter
    #lire la température

    #lire la pression

    #lire l'humidité

    #return (pression,temperature,humidite)

meteo=recupereMeteo("Le Mans")  #exécute la fonction gérant la requête GET
print("affichage du tuple", meteo) # affiche les 3 valeurs sous forme de tuple
print("pression",meteo[0]) # affiche la pression
print("temperature",meteo[1]) # affiche la température
print("humidite",meteo[2]) # affiche l'humidité
