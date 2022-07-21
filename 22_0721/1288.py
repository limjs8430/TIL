# 1288. 새로운 불면증 치료법 D2

T = int(input())


for test_case in range(1, T + 1):
    a = int(input())
    sheep = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    cnt = 0
    while True:
        if 0 not in sheep:
            break
        else:
            # 받아온 숫자 a를 cnt만큼 곱해서 문자형으로 바꿔준다.
            cnt +=1
            num = str(a*cnt)
            # 문자형으로 바꾼 num으로 포문을 돌려준다.
            for idx in range(len(num)):
                # 초기값이 모두 0으로 10개가 설정된 함수를 갱신해준다. 
                sheep[int(num[idx])] = 1
        
    print(f'#{test_case} {num}')
