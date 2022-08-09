# https://www.acmicpc.net/problem/2897

n, m = map(int, input().split())

li = [list(input()) for _ in range(n)]

dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]
answer = [0] * 6

for i in range(n):
    for j in range(m):
        # 만약 시작점이 #이 아니라면
        if li[i][j] != '#':
            cnt = 1
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx >= n or ny >= m:
                    cnt = 0
                    break
                elif li[nx][ny] == '#':
                    cnt = 0
                    break
                else:
                    if li[nx][ny] == 'X':
                        cnt += 1
            answer[cnt] += 1
            
for x in range(1, 6):
    print(answer[x])