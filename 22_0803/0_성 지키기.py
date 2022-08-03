# https://www.acmicpc.net/problem/1236

from sys import stdin

N, M = map(int, stdin.readline().split())

list_castle = []
N_cnt = [0] * N
M_cnt = [0] * M

for _ in range(N):
    list_M = list(stdin.readline().strip())
    list_castle.append(list_M)

for i in range(N):
    for j in range(M):
        if list_castle[i][j] == 'X':
            N_cnt[i] = 1
            M_cnt[j] = 1

print(max(N_cnt.count(0), M_cnt.count(0)))
