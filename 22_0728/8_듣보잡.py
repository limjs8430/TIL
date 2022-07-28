# https://www.acmicpc.net/problem/1764

N, M = map(int, input().split())

d_dict = {}
b_dict = {}
answer = []

# 듣도 못한 사람의 수 N
for i in range(N):
    d_name = input()
    d_dict[d_name] = 1

# 보도 못한 사람의 수 M - (N+2)
for j in range(M):
    b_name = input()
    key = d_dict.keys()
    if b_name in key:
        answer.append(b_name)

answer.sort()
print(len(answer))
for i in answer:
    print(i)