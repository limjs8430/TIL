# https://www.acmicpc.net/problem/9325

T = int(input())

for _ in range(T):
    s = int(input())
    n = int(input())
    opt = 0
    while n != 0:
        q, p = map(int, input().split())
        opt += (q * p)
        n -= 1
    print(s + opt)