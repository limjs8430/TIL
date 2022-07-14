# 문제 17)
# 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
# .upper(), .swapcase() 사용 금지


word = 'banana'

# 소문자를 대문자로 바꾸어주는 함수 선언
def change(n):
    # 비어있는 new_word 선언
    new_word = ''
    for idx in range(0, len(n)):
        # 입력받은 값을 하나씩 잘라 임시저장변수에 소문자로 만드는 식을 넣어준다
        # chr는 할당된 숫자에 맞는 아스키코드를 
        # ord는 할당된 아스키 코드에 맞는 숫자를 가져온다
        # 소문자에서 32를 빼주면 대문자가 된다.
        change_word = chr(ord(n[idx]) - 32)
        new_word += change_word
    return new_word

print(change(word))