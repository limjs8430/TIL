# https://www.acmicpc.net/problem/7785

# 출입 기록 수가 

T = int(input())
SG = {}
result = []

for i in range(1, T+1):
    name, status = input().split()
    SG[name] = status

for key, value in SG.items():
    if value == 'enter':
        result.append(key)

result.sort(reverse=True)

for idx in result:
    print(idx)