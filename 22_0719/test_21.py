# 주어진 숫자를 뒤집은 결과를 출력하시오. 
# * 문자열이 아닌 숫자로 활용해서 풀어주세요. str() 사용 금지

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
    # count자리 수에서 가장 큰 자리수를 count-idx자리 수로 만들어주는 계산식
    # ex) 12345는 다섯자리 수라서 count가 5인데
    # 첫번째 자리인 1을 10의 (count - idx)승을 해주면 10의 0승 즉 1의 자리수가 된다.
    # 이런식으로 숫자가 뒤집힌다.
    plus += (mok*(10**(count-idx)))

print(plus)