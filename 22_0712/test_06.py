numbers = [0, 20, 100]

#음의 무한대로 초기화
max = float("-inf")

for i in numbers:
    temp = i
    if max <= temp:
        max = temp

print(max)