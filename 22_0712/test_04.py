n = 10
a = 1
result = 1
while a<n:
    a += 1
    result *= a

print(result)

result = 1

for i in range(1, n+1):
    result *= i
print(result)
