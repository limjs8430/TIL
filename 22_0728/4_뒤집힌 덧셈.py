# https://www.acmicpc.net/problem/1357


# 숫자가 주어지면 거꾸로 뒤집는다
# 처음 숫자가 0이면 제거한다.

X, Y = map(int, input().split())

def REV(x):
    result = ''
    while x:
        result += str(x%10)
        x //= 10
    
    return int(result.lstrip("0"))


print(REV(REV(X) +REV(Y)))