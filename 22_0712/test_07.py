numbers = [0, 20, 100]

#양의 무한대로 초기화
min = float("inf")

for i in numbers:
    temp = i
    if min >= temp:
        min = temp

print(min)