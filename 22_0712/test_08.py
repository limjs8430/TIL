numbers = [0, 80, 120, 20, 100, 101]

# 음의 무한대로 초기화
first = float("-inf")
second = float("-inf")

for n in numbers:
    if first <= n:
        second = first
        first = n
        #print('첫번째')
        #print(first)
        #print(second)
    elif second < n < first:
        second = n
        #print('두번째')
        #print(first)
        #print(second)

#print('두번째로 높은 값은')
print(second)