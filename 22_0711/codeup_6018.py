## 문자열(a)를 특정 단위로 자른다
a = '1, 2, 3'
print(a.split())

## 문자열(a)를 특정 단위(:)로 자른다
a = '10:20'
numbers = a.split(':')
print(numbers)

print(numbers[0], numbers[1], sep='^')
