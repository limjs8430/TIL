# 2029. 몫과 나머지 출력하기 D1

T = int(input())

for test_case in range(1, T + 1):
    a = list(map(int, input().split()))
    x = a[0] // a[1]
    y = a[0] % a[1]
    print(f'#{test_case} {x} {y}')