# 2050. 알파벳을 숫자로 변환 D1

char = input()

for chr in char:
    num = ord(chr) - 64
    print(num, end=' ')