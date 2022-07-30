


# len_ = 암호문의 길이
# ori_ = 원본 암호문
# test_number = 명령어의 갯수
# testing = 명령어


for test_case in range(1, 11):
    len_ = int(input())
    ori = list(map(int, input().split()))
    test_number = int(input())
    testing = list(map(str, input().split()))

    for i in range(len(testing)):
        # I가 나오면
        if testing[i] == 'I':
            where = int(testing[i+1])
            #j는 i다음부터 i다다음
            # i가 0에나오면
            # 1 ~ 5
            # 2씩 더해주면 
            # 실제로는 testing[3] 부터 testing[7] 3 4 5 6 7 다섯개
            # I가 testing[8]에 나오면
            # testing 9는 8 testing 10은 6
            # 11부터 16까지
            for j in range(i + 3 , i + 3 + int(testing[i+2])):
                ori.insert(where, int(testing[j]))
                where += 1
    print(f'#{test_case} ', end='')
    for i in range(10):
        print(ori[i], end=' ')
