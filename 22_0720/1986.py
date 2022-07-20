# 1986. 지그재그 숫자 D2

T = int(input())

for idx in range(1, T+1):
    count = 0
    cnt = 1
    N = int(input())
    for Num in range(1, N+1):
        Num *= cnt
        count += Num
        cnt *= -1
    print(f'#{idx} {count}')