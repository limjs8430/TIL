# https://www.acmicpc.net/problem/2798

N, M = map(int, input().split())

li = list(map(int, input().split()))

hap = 0

for i in range(0, N-2):
    if hap == M:
        break
    else:
        for j in range(i+1, N-1):
            if hap == M:
                break
            else:
                for k in range(j+1, N):
                    if (li[i] + li[j] + li[k]) > M:
                        continue
                    elif (li[i] + li[j] + li[k]) == M:
                        hap = M
                        break
                    else:
                        if M -(li[i] + li[j] + li[k]) < M - hap:
                            hap = li[i] + li[j] + li[k]
print(hap)
