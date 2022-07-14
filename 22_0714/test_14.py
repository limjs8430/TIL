# 문제 14)
# 문자열 word가 주어질 때, 해당 문자열에서 a 개수를 구하세요.
# count() 메서드 사용 금지

# 각 word_n 변수에 테스트 문자열선언
word_1 = 'apple'
word_2 = 'banana'
word_3 = 'kiwi'

# 문자열에 a가 있을때 숫자를 카운팅해주는 함수 a 선언
def a(n):
    count_a = 0
    for idx in range(0, len(n)):
        if n[idx] == 'a':
            count_a += 1
    return count_a

# a함수에 각 변수 선언 후 출력
print(a(word_1))
print(a(word_2))
print(a(word_3))

