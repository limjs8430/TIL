import random

print('나이를 알려드립니다')
name = input('이름을 입력해주세용:  ')
# 이름마다 똑같은 숫자가 있으면 좋겠다...
# ord() # 문자를 숫자로
# 합한 값을 가져가면 이름마다 같을거다.
random.seed(sum(map(ord, name)))
# choice(a)는 하나 고르기
# sampe(a, b)는 a에서 b개 고르기
print(f'{random.choice(range(10, 90))}살')