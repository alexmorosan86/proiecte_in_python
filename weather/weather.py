import requests
import json
# https://www.weatherbit.io/

def print_weather(city):
  url = 'https://api.weatherbit.io/v2.0/current'
  params = {'city': city, 'key': '1ab5e9499298416b97674b2facdaeb1c'}
  output = requests.get(url, params)
  print(output)
  body = json.loads(output.content)
  # print(body)
  data = body['data'][0]
  print('clouds: ' + str(data['clouds']))
  print('Description: ' + data['weather']['description'])
  print('temperature: ' + str(data['temp']) + 'C')


print_weather('Suceava,RO')


