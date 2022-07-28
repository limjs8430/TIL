# https://www.acmicpc.net/problem/5622

dial = ['1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ', '0']

T = input()
cnt = 0
for i in range(len(T)):
    for idx in dial:
        if T[i] in idx:
            cnt += dial.index(idx) + 2

print(cnt)