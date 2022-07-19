# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 

print('양의 정수를 입력해주세요')
a = int(input())
# b에 a값을 넣어준다.
b = a
count = 0
plus = 0
# 나눴을때 1이하가 되면 브레이크를 걸어서 count를 출력
while True:
    a /= 10
    count += 1
    if a < 1:
        break

# count부터 0까지 -1씩 등차수열
for idx in range(count, 0, -1):
    # mok은 b값에 10의 idx-1승을 해준 몫
    mok = b//(10**(idx-1))
    # b는 10의 idx-1승을 해준 나머지를 계속해서 갱신해준다.
    b %= (10**(idx-1))
    # 계속해서 더한값을 갱신해준다.
    plus += mok

print(plus)