# https://www.acmicpc.net/problem/15953

from sys import stdin

T = int(stdin.readline())

kakao_2017 = [1, 3, 6, 10, 15, 21]
price_2017 = [500, 300, 200, 50, 30, 10]
kakao_2018 = [1, 3, 7, 15, 31]
price_2018 = [512, 256, 128, 64, 32]

for _ in range(T):
    result = 0
    X, Y = map(int, stdin.readline().split())
    for i in range(len(kakao_2017)):
        if X > 21 or X == 0:
            break
        elif X <= kakao_2017[i]:
            result += price_2017[i]
            break
    for j in range(len(kakao_2018)):
        if Y > 32 or Y == 0:
            break
        elif Y <= kakao_2018[j]:
            result += price_2018[j]
            break
    print(result*10000)
