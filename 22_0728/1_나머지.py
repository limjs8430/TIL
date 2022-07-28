# https://www.acmicpc.net/problem/3052

Remainder = []
for i in range(1, 11):
    T = int(input())
    Remainder.append(T % 42)

print(len(set(Remainder)))