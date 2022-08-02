# https://www.acmicpc.net/status?user_id=limjs8430&problem_id=2776&from_mine=1

from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    stdin.readline()
    S1_list = set(map(int, stdin.readline().split()))
    stdin.readline()
    S2_list = list(map(int, stdin.readline().split()))

    for i in S2_list:
        print(1 if i in S1_list else 0)