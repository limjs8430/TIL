# 예제 1
# 숫자 n을 받아 세제곱 결과를 반환하는 함수 cube를 정의하시오. 
# cube 함수를 호출하여 12의 세제곱 결과를 출력하시오

# 입력
a = int(input())

# 함수 
def cube(n):
    # x ** y 는 x의 y승
    return n**3

# result에 aaa함수에 a를 넣은 값 저장
result = cube(a)
# 결과값 출력
print(result)