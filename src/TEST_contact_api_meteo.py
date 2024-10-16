import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/"
WEATHER = "weather?"
AIR_POLLUTION = "air_pollution?"
API_KEY = open('src/METEO_API_KEY', 'r').read()
LAT, LON = str(46.77674895365731), str(4.846318794200057)
#CITY = 'Chalon-sur-Saône'
LANG = 'fr'
AIR_QUALITY_INDEX = {1 : 'Bonne',
                     2 : 'Correcte',
                     3 : 'Moyenne',
                     4 : 'Mauvaise',
                     5 : 'Exécrable'}


def kelvin_to_celsius(kelvin):
    return kelvin - 272.15

def ms_to_kmh(ms):
    return 3600/1e3 * ms


url_meteo = BASE_URL + WEATHER + "appid=" + API_KEY + "&lat=" + LAT + "&lon=" + LON + "&lang=" + LANG
url_air = BASE_URL + AIR_POLLUTION + "appid=" + API_KEY + "&lat=" + LAT + "&lon=" + LON

response_meteo = requests.get(url_meteo).json()
response_air = requests.get(url_air).json()

temp_kelvin = response_meteo['main']['temp']
temp_celsius = kelvin_to_celsius(temp_kelvin)

feels_like_kelvin = response_meteo['main']['feels_like']
print(feels_like_kelvin)
feels_like_celsius = kelvin_to_celsius(feels_like_kelvin)

sunrise = dt.datetime.fromtimestamp(response_meteo['sys']['sunrise']+response_meteo['timezone'],dt.timezone.utc)
sunset = dt.datetime.fromtimestamp(response_meteo['sys']['sunset']+response_meteo['timezone'],dt.timezone.utc)

humidity = response_meteo['main']['humidity']
pressure = response_meteo['main']['pressure']

temp_min = kelvin_to_celsius(response_meteo['main']['temp_min'])
temp_max = kelvin_to_celsius(response_meteo['main']['temp_max'])

desc_1 = response_meteo['weather'][0]['main']
desc_2 = response_meteo['weather'][0]['description']

visibility = response_meteo['visibility']

wind_speed = response_meteo['wind']['speed']
wind_direction = response_meteo['wind']['deg']
wind_gust = response_meteo['wind']['gust']

clouds = response_meteo['clouds']['all']


air_quality_index = response_air['list'][0]['main']['aqi']

print(response_meteo)
print(response_air)
print(f'Météo actuelle à l\'Usinerie: {desc_2}\n \
      Température : réelle : {round(temp_celsius,2)}°C, ressentie : {round(feels_like_celsius,2)}, min : {round(temp_min,2)}°C, max : {round(temp_max,2)}°C\n \
      Lever du soleil : {sunrise}\n \
      Coucher du soleil : {sunset}\n \
      Humidité : {humidity}%, Pression : {pressure}hPa\n \
      Visibilité : {visibility/1e3}km, couverture nuageuse : {clouds}%\n \
      Vent : {ms_to_kmh(wind_speed)}km/h, {wind_direction}°, avec des rafales à {ms_to_kmh(wind_gust)}km/h\n \
      Qualité de l\'air : {AIR_QUALITY_INDEX[air_quality_index]}')    
 
""" 

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