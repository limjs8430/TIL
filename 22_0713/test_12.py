# 문제 12
# 주어진 문자열 word가 주어질 때, 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.

word = 'apple'

# 스트링을 ''로 설정해준다
string = ''

# word에 있는 단어를 쪼개 pple에 넣어준다.
for pple in word:
    # word에서 쪼개서 가져온 char 알파벳이 a가 아닐시 스트링에 하나씩 더해준다.
    if pple != 'a':
        string += pple

print(string)