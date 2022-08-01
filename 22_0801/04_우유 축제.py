# https://www.acmicpc.net/problem/14720


# 딸 초 바

# 처음에는 딸기우유를 마신다 
# 딸 다음에는 초
# 초 다음에는 바
# 바 다음에는 딸
# 우유거리가 있고 전진만가능 선택은 마시고 안마시고 둘중하나
# 각 숫자별로 파는 품목이 정해져있음
# 최대로 우유를 마시는 수

from sys import stdin

T = int(stdin.readline())

result = 0
point = 0


for i in range(1, T+1):
    milk = list(map(int, stdin.readline().split()))
    
    for j in milk:
        if point == 0 and j == 0:
            point += 1
            result += 1
        elif point == 1 and j == 1:
            point += 1
            result += 1
        elif point == 2 and j == 2:
            point -= 2
            result += 1
        else:
            continue

print(result)




