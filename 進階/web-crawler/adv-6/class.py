import requests
import os
import sys

os.chdir(sys.path[0])

api_key = "0b901c6525e69d08f2619349785fadfb"  #API key

base_url = "https://api.openweathermap.org/data/2.5/weather?"
city_name = input('enter city name:')
units = "metric"
lang = 'zh_tw'

send_url = base_url
send_url += "appid=" + api_key
send_url += "&q=" + city_name
send_url += "&units" + units
send_url += "&lang=" + lang
print(send_url)
response = requests.get(send_url)
info = response.json()
print(info)
print(info["name"])
print(info['main']['temp'])
print(info['weather'][0]['description'])

if 'main' in info.keys():
    icon_code = info['weather'][0]['icon']
    icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
    response = requests.get(icon_url)
    with open(f'{icon_code}.png', "wb") as icon_file:
        icon_file.write(response.content)
else:
    print("city not found")