# 2071. 평균값 구하기 D1

T = int(input())

for test_case in range(1, T + 1):
    a = list(map(int, input().split()))
    x = 0
    for idx in range(0, len(a)):
        x += a[idx]
    print(f'#{test_case} {round(x/len(a))}')
        
