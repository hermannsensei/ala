import requests, json 
api_key = "cf3fbdcb06adfae47832bb8815b75041"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "Casablanca" 
complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
response = requests.get(complete_url) 
x = response.json() 
if x["cod"] != "404":
    y = x["main"]
    current_temperature = round(y["temp"]-273.15,4)
    current_humidiy = y["humidity"]
    d = x ["wind"]
    current_wind_speed = d["speed"]
else: 
	print(" City Not Found ")