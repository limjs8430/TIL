# 리스트
a = [10, 1, 100]
# 정렬(sort)
new_a = a.sort()
print(a, new_a)
# [1, 10, 100] None
# 리스트 메서드를 활용하면, 그 메서드를 정렬된 상태로 변경(원본 변경)
# return되는 것은 None

# 리스트
b = [10, 1, 200]
# 정렬(sort)
new_b = sorted(b)
print(b, new_b)
# [10, 1, 100] [1, 10, 100]
# sorted 함수를 활용하면, 원본을 변경하지 않음
# return되는 것은 정렬된 리스트

# 실제 활용 코드는 
a = [10, 1, 100]
a.sort()
# a를 정렬된 상태로 활용

b = [10, 1, 100]
b = sorted(b)
# b를 정렬된 상태로 활용

# .find(x)
# x의 첫 번째 위치를 반환. 없으면, -1을 반환함
print('apple'.find('p'))
# 1
print('apple'.find('k'))
# -1

# .index(x)
# x의 첫 번째 위치를 반환. 없으면, 오류 발생
index_p = 'apple'.index('p')
print(index_p)
# 1
# index_k = 'apple'.index('k')
# print(index_k)
# 에러 발생




# 문자열 변경


# .strip([chars])
# 특정한 문자들을 지정하면
# 양쪽을 제거하거나(strip), 왼쪽은 제거(lstrip), 오른쪽 제거(rstrip)
# 문자열을 지정하지 않으면 공백을 제거함


# .split(sep=None, maxsplit = -1)
# 문자열을 특정한 단위로 나눠 리스트로 반환**
# sep이 None 이거나 지정되지 않으면 연속된 공백문자를 단일한 공백문자로 간주하고,
# 선행 / 후행 공백은 빈 문자열에 포함시키지 않음.
# maxsplit이 -1인 경우에는 제한이 없음.
'a, b, c'.split(' ')
#['a, b. c]
'a b c'.split() # 기본 공백
# ['a', 'b', 'c']

# 'separator'.join([iterable])
# 반복가능한(iterable) 컨테이너 요소들을 separator(구분자)로 합쳐 문자열 반환
# iterable에 문자열이 아닌 값이 있으면 TypeError 발생
''.join(['3', '5'])
# 35
names = ','.join(['홍길동', '김철수']) 
print(names)

# numbers = ' '.join([10, 20, 30])
# 이건 타입으로 인한 오류
# 따라서 map을 활용하여 str형식으로 변환해준다.
numbers = ' '.join(map(str, [10, 20, 30]))
print(numbers)


# 기타 변경
# 문자열 변경 예시
# msg = 'hI! Everyone.'
# print(msg)
# print(msg.capitalize())
# print(msg.title())
# print(msg.upper()) # 대문자
# print(msg.lower()) # 소문자
# print(msg.swapcase()) # 대 <--> 소문자

# hI! Everyone.
# Hi! everyone.
# Hi! Everyone.
# HI! EVERYONE.
# hi! everyone.
# Hi! eVERYONE.


# 값 추가
# .extend('iterable')
# 리스트에 iterable의 항목을 추가함

# a = ['apple']
# 오류가 난다.
# a.extend('banana', 'mango')
# 하나로 넣어야한다.
# a.extend(['banana', 'mango'])
# print(a)
# ['apple', 'banana', 'mango']


# a.extend('banana')
# print(a)
# ['apple', 'b', 'a', 'n', 'a', 'n', 'a']


# .insert(i, x)
# 정해진 위치 i에 값을 추가함

# cafe = ['s', 't']
# ['s', 't']
# cafe.insert(0, 'start')
# ['start', 's', 't']


# cafe = ['s', 't']
# ['s', 't']
# cafe.insert(10000, 'end')
# ['s', 't', 'end']
# 리스트의 길이보다 큰 경우 맨 뒤로

# .remove(x)
# 리스트에서 값이 x인 것 삭제
# numbers = [1, 2, 3, 'hi']
# [1, 2, 3, 'hi']
# numbers.remove('hi')
# [1, 2, 3]
# 없는 경우 ValueError

# .pop(i)
# 정해진 위치 i에 있는 값을 삭제하고, 그 항목을 반환함
# i가 지정되지 않으면, 마지막 항목을 삭제하고 반환함

# numbers = ['hi' ,1, 2, 3 ]
# pop_number = numbers.pop()
# 3
# ['hi', 1, 2]

# numbers = ['hi' ,1, 2, 3 ]
# pop_number = numbers.pop(0)
# 'hi'
# print(numbers)
# [1, 2, 3]


# .clear()
# numbers = [1, 2, 3]
# numbers.clear()
# []


# 탐색 및 정렬
# .index(x)
# x값을 찾아 해당 index 값을 반환
# numbers = [1, 2, 3, 4]
# [1, 2, 3, 4]
# numbers.index(3)
# 2
# numbers.index(100)
# 없는값이라 오류 발생

# count(x)
# 원하는 값의 개수를 반환함
# numbers = [1, 2, 3, 1, 1]
# [1, 2, 3, 1, 1]
# numbers.count(1)
# 3
# numbers.count(100)
# 없는값이라 0이 반환

# .sort()
# 원본 리스트를 정렬함. None 반환
# sorted 함수와 비교할 것


# .reverse()
# 순서를 반대로 뒤집음(정렬하는 것이 아님), None 반환.
# numbers = [3, 2, 5, 1]
# result = numbers.reverse()
# print(numbers, result)
# [1, 5, 2, 3] None



