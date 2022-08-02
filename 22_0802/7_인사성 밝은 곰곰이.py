

from sys import stdin

T = int(stdin.readline().strip())
gom = []
cnt = 0
E = 'ENTER'

for _ in range(T):
    chat = stdin.readline().strip()
    if chat == E:
        cnt += len(set(gom))
        gom.clear()
    else:
        gom.append(chat)

print(cnt + len(set(gom)))