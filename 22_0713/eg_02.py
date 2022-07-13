# 예제 2
# 가로와 세로의 길이를 각각 a, b로 받아 사각형 넓이와 둘레를 함께 반환하는 함수 rectangle을 정의하시오. 
# 사각형이 가로가 20, 세로가 30일 때의 결과를 출력하시오.

# * 사각형 넓이 : 가로 * 세로 
# * 사각형 둘레 : (가로 + 세로) * 2

# 입력받을 a, b를 선언
a, b = input().split(',')
a = float(a)
b = float(b)

# 직사각형의 넓이와 둘레 함수
def rectangle(x, y):
    a = x * y
    b = (x + y)*2
    return a, b

# 넓이와 둘레를 각각 저장 후 출력
area, perimeter = rectangle(a, b)
print(area)
print(perimeter)