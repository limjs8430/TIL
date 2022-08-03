# https://www.acmicpc.net/problem/5533

from sys import stdin

T = int(stdin.readline())

# 세장의 카드 리스트
point_list = []

# 점수를 저장하는 리스트
get_point = [0] * T
for _ in range(T):
    point = list(map(int, stdin.readline().split()))
    point_list.append(point)

for i in range(T):
    for j in range(3):
        # 현재 비교하는 카드를 ing에 선언해주고
        ing = point_list[i][j]
        cnt = 1
        for k in range(T):
            # i와 k가 같을때는 동일한 카드일때는 다음 카드를 확인
            if k == i:
                continue
            # 카드 번호가 중복되면 cnt를 0으로 바꿔주고 해당카드 비교 중단
            elif point_list[k][j] == ing:
                cnt = 0
                break
            # break가 나왔거나 모든 카드를 확인후 cnt가 1이면 포인트를 더해준다.
        if cnt == 1:
            get_point[i] += ing
print(*get_point, sep='\n')