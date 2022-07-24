# pip install requests
from urllib import response
import requests
# URL로
order_currency = 'ALL'
payment_currency = 'KRW'
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'

response = requests.get(URL).json()

coins = response.get('data')

for coin in coins:
    if coin == 'date':
        continue
    print(coin, coins.get(coin).get('closing_price'))