# https://www.acmicpc.net/problem/1100

from sys import stdin

chess = [list(stdin.readline().strip()) for _ in range(8)]
cnt = 0

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0 and chess[i][j] == 'F':
            cnt += 1
            
print(cnt)