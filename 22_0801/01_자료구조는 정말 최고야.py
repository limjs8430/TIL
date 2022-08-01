# https://www.acmicpc.net/problem/23253

# 교과서 N권을 M개의 더미로

# 교과서는 1 부터 N번까지 번호로 구분

# 맨 위에 교과서만 꺼낼 수 있다.
# 꺼낸 교과서를 꺼내서 1부터 오름차순으로 정렬할수있어야 YES
# 아니면 NO
# 즉 내림차순으로 리스트가 정렬되어있어야 한다.


from sys import stdin

N, M = map(int, stdin.readline().split())

result = True

for _ in range(M):
    stdin.readline()
    dumi_list = list(map(int, stdin.readline().split()))
    # 더미에 쌓인 교과서의 번호가 순서대로 주어지는데
    # 주어진 번호가 내림차순으로 정렬했을때와 같아야만 올바른 순서대로 교과서를 꺼낼 수 있다.
    if dumi_list != sorted(dumi_list, reverse=True):
        result = False
        break

print('Yes' if result else 'No') 