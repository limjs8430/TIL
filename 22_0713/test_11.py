# 문제 11
# 2단부터 9단까지 반복하여 구구단을 출력하세요.
# * 문자열 출력시 f-string을 활용하면 편하게 작성할 수 있습니다.

# f-string을 사용하지 않은것
# 단을 설정한다 2~9(2이상 10미만 )
for dan in range(2, 10):
    # 현재 출력하는 단이 몇단인지 매 단마다 출력해준다.
    print(dan, '단', sep=' ')
    # 각 단마다 곱하는 숫자를 설정해준다 1이상 10미만
    for n in range(1, 10):
        print(dan, ' x ', n, ' = ', dan * n, sep='')


# f - 스트링을 사용한것
for dan in range(2, 10):
    # f스트링을 사용했다
    # ''나 ""앞에 f를 붙여 f-string을 사용하면 {}안에 변수를 입력할수있다.
    print(f'{dan}단')  
    for n in range(1, 10):
        print(f'{dan} x {n} = {dan * n}')