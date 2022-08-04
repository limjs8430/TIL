# https://www.acmicpc.net/problem/1652

from sys import stdin

N = int(stdin.readline())
li = [list(stdin.readline().strip()) for _ in range(N)]
dot = '.'
result = [0] * 2

for i in range(N):
    cnt_X = 0
    cnt_Y = 0
    for j in range(N):
        if li[i][j] == dot:
            cnt_X += 1
            if cnt_X == 2:
                result[0] += 1
                break
        else:
            cnt_X = 0
    for j in range(N):
        if li[j][i] == dot:
            cnt_Y += 1
            if cnt_Y == 2:
                result[1] += 1
                break
        else:
            cnt_Y = 0
print(*result, sep=' ')