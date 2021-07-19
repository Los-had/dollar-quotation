import requests
from time import sleep

print('This program print the dollar quotation each 30 seconds')
while True:
  url = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
  url = url.json()

  dollar = url['USDBRL']['bid'].replace('.', ',')
  sleep(30)
  print(f'Dollar quotation: {dollar}')
