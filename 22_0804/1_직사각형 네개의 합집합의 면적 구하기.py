# https://www.acmicpc.net/problem/2669

from sys import stdin

li = [[0] * 100 for _ in range(100)]

for _ in range(4):
    x, y, p, q = map(int, stdin.readline().split())
    for i in range(x, p):
        for j in range(y, q):
            li[i][j] = 1

print(sum(map(sum, li)))
