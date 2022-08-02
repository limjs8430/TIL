# https://www.acmicpc.net/problem/2750

from sys import stdin

N = int(stdin.readline())

number = []

for _ in range(N):
    number.append(int(stdin.readline()))

result = sorted(number)

print(*result, sep='\n')
    
