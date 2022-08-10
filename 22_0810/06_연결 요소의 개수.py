# https://www.acmicpc.net/problem/11724

from collections import deque
import sys

# 모든 input()대신 stdin.readline()을 사용하면 시간이 절약된다고합니다.
# 다만 input()을 바꾸기 귀찮을땐 아랫 라인처럼 사용해도 된다고 합니다.
input = sys.stdin.readline

def bfs(number):
    queue = deque([number])
    visited[number] = True
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

N, M = map(int, input().split())

# grapth를 N까지 초기화시켜준다.
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    # u와 v를 받아서 그래프에 대칭으로 넣어준다.
    u , v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)
cnt = 0

for i in range(1, N+1):
    if not visited[i]:
        if not graph[i]:
            cnt += 1
            visited[i] = True
        else:
            bfs(i)
            cnt += 1
    
print(cnt)
# print(graph)
# print(visited)