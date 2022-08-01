# https://www.acmicpc.net/problem/2902

from sys import stdin

Name = list(stdin.readline().strip())
result = []

result.append(Name[0])
for i in range(1, len(Name)):
    if Name[i] == '-':
        result.append(Name[i+1])

print(*result, sep='')