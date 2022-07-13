# 문제 13

# 주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.

# word를 받는다
word = 'apple'

# rev라는 변수에 word의 길이 -1 이하부터 -1 초과까지 -1씩 더해준다.
for rev in range(len(word) - 1 , -1, -1):
    # word[rev]를 줄바꿈없이 출력해준다.
    print(word[rev], end='')