# https://api.coingecko.com/api/v3/exchange_rates
# compute the exchange rate of bitcoin in eur and usd
# write tests for the compute function mocking the API

import requests

def main():

  response = requests.get('https://api.coingecko.com/api/v3/exchange_rates')
  # print the object, see the response code
  print(response)

  # print the content of the object
  values = response.json()

  # print the btc info
  btc = values['rates']['btc']
  # print(values['rates']['btc']

  # print the eur info
  eur = values['rates']['eur']
  # print(values['rates']['eur']

  # print the dollar info
  usd = values['rates']['usd']
  # print(values['rates']['usd']

  # compute euro in btc and usd in btc

  print('1BTC is ' + str(eur['value']) + eur ['unit'])
  print('1Btc is ' + str(usd['value']) + usd ['unit'])

def get_value_in_euro():
  response = requests.get('https://api.coingecko.com/api/v3/exchange_rates')
  values = response.json()
  eur = values['rates']['eur']
  return eur['value']

main()



