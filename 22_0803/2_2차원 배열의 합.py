# # https://www.acmicpc.net/problem/2167

# from sys import stdin

# N, M = map(int, stdin.readline().split())

# matrix = [list(map(int, stdin.readline().split())) for _ in range(N)]
# sum_matrix = [[0]*(M) for _ in range(N)]

# K = int(stdin.readline())
# result = [0] * K
# for p in range(K):
#     i, j, x, y = map(int, stdin.readline().split())
#     for n in range(i-1, x):
#         for m in range(j-1, y):
#             result[p] += matrix[n][m]

# print(*result, sep='\n')    

# 위 코드는 시간초과

from sys import stdin

N, M = map(int, stdin.readline().split())

matrix = [list(map(int, stdin.readline().split())) for _ in range(N)]
# 배열의 누적합을 저장할 배열
sum_matrix = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        sum_matrix[i][j] = matrix[i-1][j-1] + sum_matrix[i-1][j] + sum_matrix[i][j-1] - sum_matrix[i-1][j-1]


K = int(stdin.readline())
for _ in range(K):
    i, j, x, y = map(int, stdin.readline().split())
    # 여태까지 더한값에 행-1 열-1만큼의 합만큼 제하고 두 부분의 공통만큼 더해준다.
    print(sum_matrix[x][y]-sum_matrix[x][j-1]-sum_matrix[i-1][y]+sum_matrix[i-1][j-1])