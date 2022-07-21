# 1926. 간단한 369게임 D2

clap = ['3', '6', '9']

n = int(input())
for i in range(1, n+1):
    count = 0
    for j in str(i):
        if j in clap:
            count += 1
    if count > 0:
        i = '-' * count
    print(i, end=' ')
