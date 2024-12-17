'''hello, it`s my money printer'''

import requests

def print_money(url):
  callback = requests.get(url).json()

  return callback

print(print_money('https://print-money.com'))
