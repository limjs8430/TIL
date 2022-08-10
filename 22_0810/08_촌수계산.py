# https://www.acmicpc.net/problem/2644

from collections import deque


n = int(input())

a, b = map(int, input().split())

m = int(input())

graph = [[] for _ in range(n+1)]

visited = [False] * (n + 1)

result = []

for _ in range(m):
    x, y = map(int, input().split())  
    graph[x].append(y)
    graph[y].append(x)


def dfs(people, num):
    num += 1
    visited[people] = True

    if people == b:
        result.append(num)

    for i in graph[people]:
        if not visited[i]:
            dfs(i, num)

dfs(a, 0)

print(result[0] - 1)