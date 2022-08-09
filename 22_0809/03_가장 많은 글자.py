# https://www.acmicpc.net/problem/1371

from sys import *

# 인풋값을 받아서 개행과 뛰어쓰기를 제거해준다.
T = stdin.read().replace('\n', '').replace(' ', '')

# 리스트 길이를 알파벳갯수만큼 생성해주고 0을 넣어준다.
li = [0] * 26


# 아스키코드를 활용해서 리스트에 넣어주고
for idx in T:
    li[ord(idx) - 97] += 1

# 가장 큰 값을 찾아서
li_max = max(li)

# 가장 큰 값인 문자 출력
for i in range(len(li)):
    if li[i] == li_max:
        print(chr(i+97), end='')