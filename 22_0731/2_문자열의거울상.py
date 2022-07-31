# 문자열의 거울상 D3

T = int(input())

for i in range(1, T+1):
    mir = list(input())
    result = []
    # 1차적으로 문자열을 뒤집어준다 위치만 좌우반전
    mir.reverse()
    for idx in mir:
        if idx == 'b':
            result.append('d')
        elif idx == 'd':
            result.append('b')
        elif idx == 'p':
            result.append('q')
        else:
            result.append('p')
    print(f'#{i} {"".join(result)}')