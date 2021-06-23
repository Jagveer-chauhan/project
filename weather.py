import requests
from datetime import datetime

api_key = 'ee04f10ef70e57759abf06783650030b'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()
if api_data['cod'] == 200:
    # create variables to store and display data
    temp_city = (api_data['main']['temp'])
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
    print("-------------------------------------------------------------")
    print("Weather Stats for - {}  || {}".format(location.upper(), date_time))
    print("-------------------------------------------------------------")
    print("Current temperature is: {:.2f} deg f".format(temp_city))
    print("Current weather desc  :", weather_desc)
    print("Current Humidity      :", hmdt, '%')
    print("Current wind speed    :", wind_spd, 'kmph')
    data = {"temperature": temp_city, "weather": weather_desc, "humidity": hmdt, "wind": wind_spd, "date": date_time}
    with open('weather.txt', 'w') as f:
        f.write("-------------------------------------------------------------\n")
        f.write("Weather Stats for - {}  || {}".format(location.upper(), date_time))
        f.write("\n------------------------------------------------------------- \n")
        for line in data:
            f.write(line)
            f.write(' -\t')
            f.write(str(data[line]))
            f.write('\n')
else:
    print("city not found")
    with open('weather.txt', 'w') as f:
        f.write('city not found')