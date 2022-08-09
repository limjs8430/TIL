# https://www.acmicpc.net/problem/1526

T = int(input())

li = ['4', '7']

while True:
    if len(str(T)) == str(T).count('4') + str(T).count('7'):
        print(T)
        break
    else:
        T -= 1