# 1989. 초심자의 회문 검사 D2

T = int(input())

for test_case in range(1, T + 1):
    a = input()
    temp = ''
    # 받은 단어의 길이로 반복문을 시작
    for idx in range(len(a) - 1, -1, -1):
        temp += a[idx]
    if a == temp :
        print(f'#{test_case} 1')
    else :
        print(f'#{test_case} 0')