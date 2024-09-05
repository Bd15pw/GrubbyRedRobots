import requests

def getWeather(city,units='metric', api_key='13ab70d1ba6b1c1421505657c5d5d548'):
  url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}'
  r = requests.get(url)
  content =r.json()
  
  with open('data.txt', 'a') as file:
    for item in content['list']:
      file.write(f"{item['dt_txt']}, {item['main']['temp']}\n")

  
  

print(getWeather(city="Warszawa"))
  