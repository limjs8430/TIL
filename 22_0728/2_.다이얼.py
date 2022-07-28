# https://www.acmicpc.net/problem/5622

T = list(input())

cnt = 0

for idx in T:
    if idx in ['1']:
        cnt += 2
    elif idx in ['A', 'B', 'C']:
        cnt += 3
    elif idx in ['D', 'E', 'F']:
        cnt += 4
    elif idx in ['G', 'H', 'I']:
        cnt += 5
    elif idx in ['J', 'K', 'L']:
        cnt += 6
    elif idx in ['M', 'N', 'O']:
        cnt += 7
    elif idx in ['P', 'Q', 'R', 'S']:
        cnt += 8
    elif idx in ['T', 'U', 'V']:
        cnt += 9
    elif idx in ['W', 'X', 'Y', 'Z']:
        cnt += 10
    else:
        cnt += 11
print(cnt)