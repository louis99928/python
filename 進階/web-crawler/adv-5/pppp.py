import requests

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