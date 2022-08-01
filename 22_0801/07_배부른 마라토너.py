# https://www.acmicpc.net/problem/10546

from sys import stdin

T = int(stdin.readline().strip())
name_dict = {}

for i in range(1, T+1):
    name = stdin.readline().strip()
    if name in name_dict:
        name_dict[name] += 1
    else:
        name_dict[name] = 1

for i in range(1, T):
    name = stdin.readline().strip()
    name_dict[name] -= 1

for p in name_dict:
    if name_dict[p] == 1:
        print(p)
        break
    else:
        continue