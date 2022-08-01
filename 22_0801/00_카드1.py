# https://www.acmicpc.net/problem/2161

T = int(input())

card_list = list(range(1, T + 1))
drop_list = []


# 제일 위에있는 카드를 드랍리스트에
# 그다음 있는 카드를 카드리스트 제일 아래로
# 이 사이클을 T - 1번 반복한다.
for i in range(1, T):
    drop_list.append(card_list.pop(0))
    card_list.append(card_list.pop(0))

print(*drop_list, *card_list)