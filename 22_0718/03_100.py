# 100을 사용자가 입력한 숫자로 나눠서 결과를 출력
number = input()

try:
    print(100/int(number))
except ZeroDivisionError:
    print('0으로 나눌 수는 없습니다.')
except ValueError:
    print('숫자형식을 입력해주세요.')
except Exception:
    print('오류')
# 작은상황부터 큰상황으로!!!!
    