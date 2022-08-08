# https://www.acmicpc.net/problem/1436

N = int(input())

# 666이 들어간 숫자중에서 N번째로 작은 숫자를 구하는 문제
# 그래서 666이 들어간 가장작은 수를 바로 구하기위해
# 인위적으로 처음 result에 665를 넣어줬습니다.
result = 665

#반복문을 입력받은 N만큼 돌립니다.(N이 계속해서 차감되서 0이되면 그만)
while N:
    #반복문 실행할때 reulst에 1을 더해주고
    result += 1
    #result값을 str화 시킨것에 666이 포함되면 N을 1씩 차감해줍니다
    if '666' in str(result):
        N -= 1

print(result)