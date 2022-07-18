# 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 
# 양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지

print('양의 정수를 입력해주세요')
a = int(input())
count = 0
# 나눴을때 1이하가 되면 브레이크를 걸어서 count를 출력
while True:
    a /= 10
    count += 1
    if a < 1:
        break

print(count)