N = 4

subset = [0] * N

for i in range(1<<N):
    for j in range(N):
        subset[j] = 1 if i & (1<<j) else 0
    print(subset)