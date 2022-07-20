# 1933. 간단한 N 의 약수 D1

N = int(input())

for idx in range(1, N+1):
    if N % idx == 0:
        print(idx, end=' ')