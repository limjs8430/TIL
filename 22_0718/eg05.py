# 아래 코드는 숫자의 길이를 구하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# TypeError: object of type 'int' has no len()
# 인트형은 길이를 구하는 타입이 아니므로 스트링타입으로 바꿔준다.
number = '22020718'
print(len(number))