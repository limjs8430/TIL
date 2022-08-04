# https://www.acmicpc.net/problem/4396

from sys import stdin

n = int(stdin.readline())

li = [list(stdin.readline().strip()) for _ in range(n)]

li_mine = [list(['.'] * (n+2)) for _ in range(n+2)]

for i in range(n):
    for j in range(n):
        li_mine[i+1][j+1] = li[i][j]

li_input = [list(stdin.readline().strip()) for _ in range(n)]

li_return = [list(['.'] * n ) for _ in range(n)]

# 여기까지가 주변에 지뢰탐색을 안하고 x를 넣었을때 0이라는 값을 리턴해주는 코드
# for i in range(n):
#     for j in range(n):
#         if li_mine[i][j] == '.' and li_input[i][j] == 'x':
#             li_return[i][j] = 0


# 조건을 좀 더 잘줬으면 하나를 없앴을거같다.
# li_mine을 삭제하고
# i와 j의 범위를 지정해주면 될거같다...

for i in range(n):
    for j in range(n):
        if li_mine[i+1][j+1] == '*' and li_input[i][j] == 'x':
            for a in range(n):
                for b in range(n):
                    if li[a][b] == '*':
                        li_return[a][b] = li[a][b]
        elif li_mine[i+1][j+1] == '.' and li_input[i][j] == 'x':
            cnt = 0
            for p in range(i-1, i+2):
                for q in range(j-1, j+2):
                    if li_mine[p+1][q+1] == '*':
                        cnt += 1
            li_return[i][j] = cnt

for rst in li_return:
    print(*rst, sep='')