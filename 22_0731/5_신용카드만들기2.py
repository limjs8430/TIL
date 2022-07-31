# 신용카드 만들기 2 D2

T = int(input())
ok = ['3', '4', '5', '6', '9']

for i in range(1, T+1):
    credit = list(map(str, input()))
    while '-' in credit:
        credit.remove('-')
    if len(credit) != 16:
        print(f'#{i} 0')
    elif credit[0] in ok:
        print(f'#{i} 1')
    else:
        print(f'#{i} 0')