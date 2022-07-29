# 직사각형의 길이를 구한다
# 주어진 숫자 세개가 같으면 나머지도 같다
# 주어진 숫자중 두개는 같고 한개가 다르면 나머지는 다른 한개이다

T = int(input())

for i in range(1, T+1):
    x = list(map(int, input().split()))
    if x.count(max(x)) == 3:
        print(f'#{i} {max(x)}')
    elif x.count(max(x)) == 2:
        print(f'#{i} {min(x)}')
    else:
        print(f'#{i} {max(x)}')


