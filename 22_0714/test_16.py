# 문제 16)
# 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
# 모음 : a, e, i, o, u 

# 각 word_n 변수에 테스트 문자열선언
word_1 = 'apple'
word_2 = 'aeiou'
word_3 = 'zxcvb'

# 문자열에 모음 있을때 숫자를 카운팅해주는 함수 a 선언
def a(n):
    count_a = 0
    for idx in range(0, len(n)):
        # 모든값에 a e i o u 모음을 or 연산자로 대입
        # if n[idx] in ['a', 'e', 'i', 'o', 'u']: 이렇게 사용해도 된다.
        if n[idx] == 'a' or n[idx] == 'e' or n[idx] == 'i' or n[idx] == 'o' or n[idx] == 'u':
            count_a += 1
            continue
    return count_a

# a함수에 각 변수 선언 후 출력
print(a(word_1))
print(a(word_2))
print(a(word_3))