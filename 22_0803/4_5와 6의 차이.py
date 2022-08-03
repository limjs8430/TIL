from dataclasses import replace

x, y = map(str, input().split())

result_5 = int(x.replace('5', '6')) + int(y.replace('5', '6'))
result_6 = int(x.replace('6', '5')) + int(y.replace('6', '5'))

print(result_6, result_5)