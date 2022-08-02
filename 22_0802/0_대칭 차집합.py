# https://www.acmicpc.net/problem/1269

from sys import stdin

stdin.readline()
A = set(map(int, input().split()))
B = set(map(int, input().split()))

result = len((A | B) - (A & B))

print(result)