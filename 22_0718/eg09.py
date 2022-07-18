# 아래 코드는 과일의 개수를 구하는 논리적 오류가 있는 코드의 일부분 입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        # fruit_count = {fruit: 1}
        # 위 코드는 하나의 키값에 계속해서 갱신해주는 코드라서 
        # 마지막에 들어간 과일만 출력하게 된다.
        # 아래 코드처럼 바꿔주면 for문에서 가져온 리스트 내용물마다
        # 새로운 키값과 값을 추가, 변경해준다.
        fruit_count[fruit] = 1
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)