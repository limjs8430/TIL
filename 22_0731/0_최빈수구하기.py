# 최빈수 구하기 D2

T = int(input())

for number in range(1, T+1):
    N = int(input())
    point = list(map(int, input().split()))
    list_point = [0] * 101
    for p in point:
        list_point[p] += 1
    max_point = 0
    for i in range(0, len(list_point)):
        if list_point[i] >= max_point:
            max_index = i
            max_point = list_point[i]
    print(f'#{number} {max_index}')