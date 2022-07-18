# > 두 수를 Input으로 받아 합을 구하는 코드이다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

numbers = input().split()
# 입력받은 number는 리스트고 저장된 값은 스트링 변수이다.

# 아래 프린트를 사용해 보면 알 수 있다.
# print(numbers)
# print(type(numbers[]))

# 따라서 map을 이용해서 리스트에 들어간 변수들을 int형으로 변환시켜주고 실행시킨다.
numbers = list(map(int, numbers))

print(sum(numbers))