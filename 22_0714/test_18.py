# 문제 18)
# 문자열 word가 주어질 때, Dictionary를 활용해서 해당 문자열에서 
# 등장한 모든 알파벳 개수를 구해서 출력하세요.


# 주어진 문자열 선언
word = 'banana'

# banana 함수 생성
def banana(n):
    # 비어있는 딕셔너리 생성
    diction = {}
    # 함수에 넣어주는 n 값을 쪼갠다
    for chr in n:
        # 조건문으로 쪼갠 단어가 딕셔너리에 있으면 값을 1 더해준다.
        if chr in diction:
            diction[chr] += 1
        # 없다면 생성해서 값을 1 넣어준다.
        else:
            diction[chr] = 1
        # 딕셔너리 diction을 리턴해준다.
    # 딕셔너리의 키와 값의 쌍으로 얻기위해 .items()를 사용해준다.
    for key, value in diction.items():
        print(key, value)
    return None

banana(word)
