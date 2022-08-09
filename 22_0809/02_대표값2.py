# https://www.acmicpc.net/problem/2587

li = []

for _ in range(5):
    li.append(int(input()))

li.sort()
print(int(sum(li)/len(li)))
print(li[2])