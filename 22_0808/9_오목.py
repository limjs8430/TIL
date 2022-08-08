# https://www.acmicpc.net/problem/2615

omok = [list(map(int, input().split())) for _ in range(19)] 

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]
clear = 0

for x in range(19):
    for y in range(19):
        if omok[x][y] != 0:
            now = omok[x][y]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                cnt = 1

                while 0 <= nx < 19 and 0 <= ny < 19 and omok[nx][ny] == now:
                    cnt += 1

                    if cnt == 5:
                        if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and omok[x - dx[i]][y - dy[i]] == now:
                            break
                        if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and omok[nx + dx[i]][ny + dy[i]] == now:
                            break
                        print(now)
                        print(x + 1, y + 1)
                        clear = cnt
                        break
                        

                    nx += dx[i]
                    ny += dy[i]

if clear != 5:
    print(0)