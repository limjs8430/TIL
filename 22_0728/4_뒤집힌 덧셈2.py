# https://www.acmicpc.net/problem/1357


# 숫자가 주어지면 거꾸로 뒤집는다
# 처음 숫자가 0이면 제거한다.

X, Y = map(str, input().split())
rev = str(int(X[::-1]) + int(Y[::-1]))
print(int(rev[::-1]))

