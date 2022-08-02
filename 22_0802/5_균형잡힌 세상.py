# https://www.acmicpc.net/problem/4949

from sys import stdin

while True :

    T = stdin.readline().rstrip()
    stack = []
    finish = '.'

    if T == finish:
        break

    for i in T :
        if i == '[' or i == '(' :
            stack.append(i)
        elif i == ']' :
            if len(stack) != 0 and stack[-1] == '[' :
                stack.pop() 
            else : 
                stack.append(']')
                break
        elif i == ')' :
            if len(stack) != 0 and stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(i)
                break
    if len(stack):
        print('no')
    else :
        print('yes')