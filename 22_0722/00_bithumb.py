# pip install requests
import requests
# URL로
order_currency = 'BTC'
payment_currency = 'KRW'
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'
# 요청을 보내서
response = requests.get(URL)
# 응답 받은 값을 가져온다.
print(response, type(response))

print(response.status_code)
print(response.text)

# 메서드 예서
# .json() 텍스트 형식의 JSON 파일을 파이썬 데이터 타입으로 변경!
print(response.json(), type(response.json()))

print('-----------------------')

data = response.json()
print(data)
# data 는 딕셔너리 => key로 접근 해요.
print(data.get('data').get('closing_price'))