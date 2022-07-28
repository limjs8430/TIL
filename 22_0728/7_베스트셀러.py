# https://www.acmicpc.net/problem/1302

T = int(input())
sell = {}
result = []


for i in range(1, T+1):
    book = input()
    if book in sell:
        sell[book] += 1
    else:
        sell[book] = 1

max_fre = max(sell.values())

for key, value in sell.items():
    if value >= max_fre:
        result.append(key)
        best = value
    
result.sort()
print(result[0])