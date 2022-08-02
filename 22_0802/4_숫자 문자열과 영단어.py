# https://school.programmers.co.kr/learn/courses/30/lessons/81301?language=python3

test = input()

number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for i, num in enumerate(number):
    if num in test:
        test = test.replace(num, str(i))
print(test)


# 제출 코드

# def solution(s):
#     number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
#     for i, num in enumerate(number):
#         if num in s:
#             s = s.replace(num, str(i))
#     return int(s)