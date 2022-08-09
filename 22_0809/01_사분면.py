# https://www.acmicpc.net/problem/9610

T = int(input())

pw = [0] * 5

for _ in range(T):
    x, y = map(int, input().split())
    
    if x > 0 and y > 0:
        pw[0] += 1
    elif x < 0 and y > 0:
        pw[1] += 1
    elif x < 0 and y < 0:
        pw[2] += 1
    elif x > 0 and y < 0:
        pw[3] += 1
    else:
        pw[4] += 1

print(f'Q1: {pw[0]}')
print(f'Q2: {pw[1]}')
print(f'Q3: {pw[2]}')
print(f'Q4: {pw[3]}')
print(f'AXIS: {pw[4]}')
