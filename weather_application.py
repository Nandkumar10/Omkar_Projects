import win32com.client as wincl
import requests
import json
speak = wincl.Dispatch("SAPI.SpVoice")
city = input("Enter the name of the City\n")
url = f"http://api.weatherapi.com/v1/current.json?key=d828954bc1b14e6284a33534232705&q={city}"
r = requests.get(url)
print(r.text)
weather_dic = json.loads(r.text)
t = (weather_dic["current"]["temp_c"])
h = (weather_dic["current"]["humidity"])
w = (weather_dic["current"]["wind_dir"])
speak.Speak(f"say'The current weather in {city} is {t} degree celsius and humidity is {h} , the direction of the wind is in {w}'")
