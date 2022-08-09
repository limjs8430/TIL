# https://www.notion.so/hphk-edu/22-edea5d6c9e9946c1924dbee716cb9df7
from pprint import *


N, M = map(int, input().split())

li = [[0]*(N+1) for _ in range(N+1)]
li_low = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    # 방향이있으니까 해당하는 방향으로
    li[x][y] = 1
    li_low[x].append(y)

pprint(li)
print(li_low)