# 아래 코드는 문자열에서 모음의 개수를 찾는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.


word = "HappyHacking"

count = 0

for char in word:
    # if문의 조건이 잘못되었다.
    # if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
    # 이렇게 or연산자를 작성해주거나
    # 아래 코드처럼 작성해주면 된다.
    if char in ['a', 'e', 'i', 'o', 'u']:
        count += 1

print(count)