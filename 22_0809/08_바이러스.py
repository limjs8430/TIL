# https://www.acmicpc.net/problem/2606

T = int(input())

N = int(input())

dic = {}

for i in range(1, T+1):
    dic[i] = set()

for j in range(1, N+1):
    x, y = map(int, input().split())
    dic[x].add(y)
    dic[y].add(x)

def dfs(start, dic):
    # start값에 1이 들어오므로 i는 2와 5
    for i in dic[start]:
        if i not in virus:
            virus.append(i)
            # print(i)
            # 재귀함수 사용
            # 2 -> 1 -> 5 -> 6 -> 3
            dfs(i, dic)

virus = []
dfs(1, dic)
print(len(virus) - 1)
# print(dic)