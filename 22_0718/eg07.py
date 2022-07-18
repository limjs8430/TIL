# 아래 코드는 평균을 구하는 논리적으로 오류가 있는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.


# 들여쓰기를 정확히 해주고 평균을 확실히 하기위해 float형을 사용하고 
# 연산자도 /로 바꿔준다.
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    # --------------------------------------------
    count += 1

print(float(total / count))