print('미세먼지 농도를 입력해주세요')

dust = int(input())

if dust > 150:
    if dust > 300:
        print('실외활동을 자제하세요.')
    print('매우나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    if dust <0:
        print('음수 값입니다.')
    else:
        print('좋음')
