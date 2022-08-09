# https://www.acmicpc.net/problem/1264

aeiou = ['a', 'e', 'i', 'o', 'u']
T = True

while T:
    check = input().lower()
    cnt = 0
    if check == '#':
        break
    else:
        for idx in check:
            if idx in aeiou:
                cnt += 1
    print(cnt)

# aeiou 리스트를 만들고
# while문을 이용해서 #이나오면 멈추고 아니면 모음 검증 시작
# 받아오는 값을 lower함수를 이용해서 모두 소문자로 변환
