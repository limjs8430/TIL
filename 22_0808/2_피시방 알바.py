# https://www.acmicpc.net/problem/1453

N = int(input())

S = list(map(int, input().split()))

result = int(len(S)) - int(len(set(S))) 

print(result)