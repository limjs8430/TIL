# https://www.acmicpc.net/problem/11286

import heapq
from sys import stdin

heap_abs = []

T = int(stdin.readline())
for _ in range(T):
    number = int(stdin.readline())
    if number == 0:
        if heap_abs:
            print(heapq.heappop(heap_abs)[1])
        else:
            print(number)
    else:
        heapq.heappush(heap_abs, (abs(number), number))

