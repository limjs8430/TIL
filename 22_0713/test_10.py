# 문제 10
# 주어진 리스트의 요소 중에서 5의 개수를 출력하시오.

numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]

# 같은 숫자일때  카운트할 변수 선언
count = 0

# 반복문 for 을 이용하여 numbers에 있는 리스트를 각각 same으로 빼온다.
for same in numbers:
    # 조건문 - 리스트에서 가져온 숫자가 5일때 1씩 카운트를 더해준다.
    if same == 5:
        count += 1

# 가져온 count를 출력한다.
print(count)