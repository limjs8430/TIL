# https://www.acmicpc.net/problem/9012

from sys import stdin

T = int(stdin.readline())

for i in range(1, T+1):
    cnt = 0
    point = 0
    PS = list(stdin.readline())

    # (가 나오면 +1
    # )가 나오면 -1
    # point가 한번이라도 0보다 작아지면 no
    while PS[cnt] != '\n' and point >= 0:
        if PS[cnt] == '(':
            point += 1
        else:
            point -= 1
        cnt +=1
        pass

    # 모든것 이후 포인트가 0이아니면 NO 맞으면 YES 출력
    print('YES' if point == 0 else 'NO')
 
