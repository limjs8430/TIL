# https://www.acmicpc.net/problem/20001


# 문제는 point += 1
# 고무오리는 point가 1 이상일때 -= 1
# 그러나 point가 0 일때는 -= 2

if input() == '고무오리 디버깅 시작':
    point = 0
    ori = True

for i in range(1, 102):
    T = input()
    if T == '고무오리 디버깅 끝':
        ori = False
    elif T == '문제':
        point += 1
    elif T == '고무오리' and point >= 1:
        point -= 1
    else:
        point += 2

    if not ori:
        break
    else:
        continue

print('고무오리야 사랑해' if point == 0 else '힝구')
