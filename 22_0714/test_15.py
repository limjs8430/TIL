# 문제 15)
# 문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.
# find() index() 메서드 사용 금지

word_1 = 'apple'
word_2 = 'banana'
word_3 = 'kiwi'

# 문자열에 a가 처음으로 나오는 위치를 알려주는 함수
def where_a(n):
    count_where_a = 0
    for idx in range(0, len(n)):        
        # idx 가 문자열의 길이와 같지 않을때
        if idx != len(n)-1:
            # 문자열에 들어있는 알파벳이 a가 아닐때 +1씩 증가
            if n[idx] != 'a':
                count_where_a += 1
            # 문자열에 들어있는 알파벳이 a일때 break를 이용해서 반복문 종료
            elif n[idx] == 'a':
                break
        # idx가 문자열의 길이와 같을때
        elif idx == len(n)-1:
             # 마지막 알파벳이 a인지 검증
             # 마지막 알파벳이 a가 아닐때
            if n[idx] != 'a':
                # count_where_a에 -1을 넣어준다.
                count_where_a = -1
            # 문자열에 들어있는 알파벳이 a일때 break를 이용해서 반복문 종료
            elif n[idx] == 'a':
                break
    # 마친 반복문에 들어있는 count_where_a를 반환
    return count_where_a

def real_where_a(n):
    count_a = 0
    for idx in range(0, len(n)):
        if n[idx] == 'a':
            count_a += 1
            print(idx , end=' ')
    print('')
    return None


print(where_a(word_1))
print(where_a(word_2))
print(where_a(word_3))

real_where_a(word_1)
real_where_a(word_2)
real_where_a(word_3)

