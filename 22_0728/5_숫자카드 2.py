# https://www.acmicpc.net/problem/10816

S = int(input())
S_card = list(map(int, input().split()))
result = {}

for i in range(0, S):
    if S_card[i] in result:
        result[S_card[i]] += 1
    else:
        result[S_card[i]] = 1

M = int(input())
M_card = list(map(int, input().split()))

for j in range(0, M):
    print(result.get(M_card[j], 0), end=' ')

