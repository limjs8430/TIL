# 1284. 수도 요금 경쟁 D2 Attack

T = int(input())

# A사의 요금은 리터당 P원
# B사의 요금은 기본요금 Q원 정해진 R리터를 넘어가면 리터당 S원 추가
# 사용량은 W리터
def water(P, Q, R, S, W):
    A = P * W
    if W <= R:
        B = Q
    else:
        B = Q + (W - R) * S
    
    if A < B:
        return A
    else:
        return B

# 입력값 변수에 넣고 프린트
for idx in range(1, T+1):
    P, Q, R, S, W = list(map(int, input().split()))
    print(f'#{idx} {water(P, Q, R, S, W)}')
