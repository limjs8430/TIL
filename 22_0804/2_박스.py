# https://www.acmicpc.net/problem/9455

from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    N, M = map(int, stdin.readline().split())
    li = [list(map(int, stdin.readline().split())) for _ in range(N)]
    result = 0
    for j in range(M):
        move_point = 0
        box_point = 0
        for i in range(N-1, -1, -1):
            # 0이면 박스 포인트가 1점 추가(위치점수 1점)
            if li[i][j] == 1:
                move_point += box_point
            # 1이면 무브 포인트가 박스포인트만큼 추가(이동한 만큼)
            else:
                box_point += 1
        result += move_point
    print(result)
