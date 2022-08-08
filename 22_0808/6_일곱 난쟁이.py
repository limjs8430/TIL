# https://www.acmicpc.net/problem/2309


li = [int(input()) for _ in range(9)]

hap = sum(li)

for i in range(9):
    if len(li) == 9:
        for j in range(i+1, 9):
            if hap - (li[i] + li[j]) != 100:
                continue
            else:
                x , y = li[i], li[j]
                li.remove(x)
                li.remove(y)
                break
    else:
        break
    
li.sort()
print(*li, sep='\n')