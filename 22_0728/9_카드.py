# https://www.acmicpc.net/problem/11652

T = int(input())

card_dict = {}
answer = []

for i in range(1, T+1):
    card = int(input())
    if card not in card_dict:
        card_dict[card] = 1
    else:
        card_dict[card] += 1

max_fre = max(card_dict.values())

for key, value in card_dict.items():
    if value == max_fre:
        answer.append(key)

answer.sort()
print(answer[0])
