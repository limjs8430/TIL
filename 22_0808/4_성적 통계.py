from collections import deque


# https://www.acmicpc.net/problem/5800

T = int(input())

for i in range(1, T+1):
    li = deque(map(int, input().split()))
    li.popleft()
    li = sorted(list(li))
    Largest_gap = 0
    for j in range(len(li) - 1):
        if li[j+1] - li[j] > Largest_gap:
            Largest_gap = li[j+1] - li[j]
        else:
            continue
    print(f'Class {i}')
    print(f'Max {max(li)}, Min {min(li)}, Largest gap {Largest_gap}')