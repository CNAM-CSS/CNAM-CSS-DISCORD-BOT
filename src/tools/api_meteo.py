import datetime as dt
import requests
import dotenv
import os

BASE_URL = "http://api.openweathermap.org/data/2.5/"
WEATHER = "weather?"
AIR_POLLUTION = "air_pollution?"
ENV = dotenv.load_dotenv()
API_KEY = str(os.getenv("METEO_API"))
LAT, LON = str(46.77674895365731), str(4.846318794200057)
#CITY = 'Chalon-sur-Saône'
LANG = 'fr'

INDEX_QUALITE_AIR = {1 : 'Bonne',
                     2 : 'Correcte',
                     3 : 'Moyenne',
                     4 : 'Mauvaise',
                     5 : 'Exécrable'}

ICONES_QUALITE_AIR = {1 : '🌳🌳🌳',
                     2 : '👍',
                     3 : '💩',
                     4 : '🚬💩🚨',
                     5 : '☠️☠️☠️'}

def kelvin_to_celsius(kelvin):
    return kelvin - 272.15

def ms_en_kmh(ms):
    return 3600/1e3 * ms

def icone_direction_vent(direction_vent):
  """Renvoie l'icône la mieux adaptée à la direction du vent

  Args:
      direction_vent (_int_): _direction du vent en °_

  Returns:
      _icône_ (_string_): _icône_
  """
  if direction_vent<22.5:
      return '⬆️'
  elif direction_vent<67.5:
      return '↗️'
  elif direction_vent<112.5:
      return '➡️'
  elif direction_vent<157.5:
      return '↘️'
  elif direction_vent<202.5:
      return '⬇️'
  elif direction_vent<247.5:
      return '↙️'
  elif direction_vent<292.5:
      return '⬅️'
  elif direction_vent<337.5:
      return '↖️'
  else:
      return '⬆️'
    
def icone_temperature(temp):
  """
  Renvoie l'icône la mieux adaptée à la température

  Args:
      temp (_int_): _Température en °C_

  Returns:
      _icône_ (_string_): _icône_
  """
  if temp<0:
      return '🧊'
  elif temp<15:
      return '🥶'
  elif temp<20:
      return '😓'
  elif temp<23:
      return '😊'
  elif temp<25:
      return '☀️'
  else:
      return '🔥🥵🔥'
  
def icone_nuages(couverture):
  """Renvoie l'icône la mieux adaptée à la couverture nuageuse

  Args:
      couverture (_int_): _Couverture nuageuse en %_

  Returns:
      _icône_ (_string_): _icône_
  """
  if couverture<10:
      return '☀️'
  elif couverture<40:
      return '🌤️'
  elif couverture<60:
      return '⛅'
  elif couverture<80:
      return '🌥️'
  else:
      return '🌫️'
    
url_meteo = BASE_URL + WEATHER + "appid=" + API_KEY + "&lat=" + LAT + "&lon=" + LON + "&lang=" + LANG
url_air = BASE_URL + AIR_POLLUTION + "appid=" + API_KEY + "&lat=" + LAT + "&lon=" + LON

def generer_message_meteo():
  reponse_meteo = requests.get(url_meteo).json()
  reponse_air = requests.get(url_air).json()

  temp_kelvin = reponse_meteo['main']['temp']
  temp_celsius = kelvin_to_celsius(temp_kelvin)

  ressenti_kelvin = reponse_meteo['main']['feels_like']
  ressenti_celsius = kelvin_to_celsius(ressenti_kelvin)

  lever_soleil = dt.datetime.fromtimestamp(reponse_meteo['sys']['sunrise']+reponse_meteo['timezone'],dt.timezone.utc)
  coucher_soleil = dt.datetime.fromtimestamp(reponse_meteo['sys']['sunset']+reponse_meteo['timezone'],dt.timezone.utc)

  humidite = reponse_meteo['main']['humidity']
  pression = reponse_meteo['main']['pressure']

  temp_min = kelvin_to_celsius(reponse_meteo['main']['temp_min'])
  temp_max = kelvin_to_celsius(reponse_meteo['main']['temp_max'])

  description_1 = reponse_meteo['weather'][0]['main']
  description_2 = reponse_meteo['weather'][0]['description']

  visibilite = reponse_meteo['visibility']
  if visibilite==10000:
      visibilite = 'maximale'
  else:
      visibilite = str(visibilite/1e3)+'km'

  vent_vitesse = reponse_meteo['wind']['speed']
  direction_vent = reponse_meteo['wind']['deg']
  vent_rafale = reponse_meteo['wind']['gust']

  nuages = reponse_meteo['clouds']['all']

  index_qualite_air = reponse_air['list'][0]['main']['aqi']

  message_titre = f'Météo de l\'Usinerie: {description_2} {icone_temperature(temp_celsius)}'
  message_temperature = f'🌡️ Réelle : {round(temp_celsius,2)}°C, ressentie : {round(ressenti_celsius,2)}°C, min : {round(temp_min,2)}°C, max : {round(temp_max,2)}°C'
  message_lever_soleil = f'🌄 Lever : {lever_soleil.strftime('%Hh%M')}'
  message_coucher_soleil = f'🌇 Coucher : {coucher_soleil.strftime('%Hh%M')}'
  message_humidite = f'😶‍🌫️ Humidité : {humidite}%, 🏋️ Pression : {pression}hPa'
  message_visibilite_nuages = f'👀 Visibilité : {visibilite}, ☁️ couverture nuageuse : {nuages}% {icone_nuages(nuages)}'
  message_vent = f'🍃 Vitesse : {round(ms_en_kmh(vent_vitesse),2)}km/h, 🧭 {direction_vent}°{icone_direction_vent(direction_vent)}, avec des 🌪️ rafales à {round(ms_en_kmh(vent_rafale),2)}km/h'
  message_air = f'🫁 {INDEX_QUALITE_AIR[index_qualite_air]} {ICONES_QUALITE_AIR[index_qualite_air]}'

  return message_titre,message_temperature,message_lever_soleil,message_coucher_soleil,message_humidite,message_visibilite_nuages,message_vent,message_air     

if __name__ == '__main__':
    print(generer_message_meteo())

""" 
Exemple message meteo

{'coord': {'lon': 4.85, 'lat': 46.7833}, 
'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}],
 'base': 'stations', 
 'main': {'temp': 294.38, 'feels_like': 294.49, 'temp_min': 294.38, 'temp_max': 294.38, 'pressure': 1012, 
 'humidity': 74, 'sea_level': 1012, 'grnd_level': 986},
   'visibility': 10000, 'wind': {'speed': 3.1, 'deg': 96, 'gust': 5.56}, 'clouds': {'all': 100}, 'dt': 1729005698, 
   'sys': {'type': 2, 'id': 2017504, 'country': 'FR', 'sunrise': 1728971911, 'sunset': 1729011225}, 
   'timezone': 7200, 'id': 3027484,
 'name': 'Chalon-sur-Saône', 'cod': 200}

"""