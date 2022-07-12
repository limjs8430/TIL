print('미세먼지 농도를 입력해주세요')

dust = int(input())

if dust > 150:
    print('매우나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')
