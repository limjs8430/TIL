# https://www.acmicpc.net/problem/5063

from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    r, e, c = map(int, stdin.readline().split())
    if r > (e - c):
        print('do not advertise')
    elif r < (e - c):
        print('advertise')
    else:
        print('does not matter')