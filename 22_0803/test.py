# https://www.acmicpc.net/problem/2167

from sys import stdin

N, M = map(int, stdin.readline().split())

matrix = [list(map(int, stdin.readline().split())) for _ in range(N)]
sum_matrix = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        sum_matrix[i][j] = matrix[i-1][j-1] + sum_matrix[i-1][j] + sum_matrix[i][j-1] - sum_matrix[i-1][j-1]



K = int(stdin.readline())
for _ in range(K):
    i, j, x, y = map(int, stdin.readline().split())
    print(sum_matrix[x][y] - sum_matrix[x][j-1] - sum_matrix[x-1][j] + sum_matrix[x-1][j-1])