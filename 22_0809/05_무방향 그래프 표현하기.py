# https://www.notion.so/hphk-edu/21-bb38e88c331a46628d5c6ee33ddcd50c

from pprint import *


N, M = map(int, input().split())

li = [[0]*(N+1) for _ in range(N+1)]
li_low = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    # 방향이없으니까 대칭이되게 
    li[x][y] = 1
    li[y][x] = 1
    li_low[x].append(y)
    li_low[y].append(x)

pprint(li)
print(li_low)