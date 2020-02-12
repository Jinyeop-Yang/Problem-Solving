"""
[S/W 문제해결 기본] 2일차 - Sum
"""
# import sys
# sys.stdin = open("input.txt", "r")

for _ in range(10):
    tc = int(input())
    MAP = [list(map(int, input().split())) for _ in range(100)]
    right_down = left_down = max_number = 0

    # 행 더하기 & 오른쪽아래 대각선 더하기 & 비교
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += MAP[i][j]
            if i == j:
                right_down += MAP[i][j]
        if temp > max_number:
            max_number = temp # 행의 합 중 가장 큰 값 저장

    # 오른쪽아래 대각선과 max_number 비교
    if max_number < right_down:
        max_number = right_down

    # 열 더하기 & 비교
    for i in range(100):
        temp = 0
        for j in range(99, -1, -1):
            temp += MAP[j][i]
            if i + j == 99:
                left_down += MAP[j][i]
        if temp > max_number:
            max_number = temp # 열의 합 중 가장 큰 값 저장

    # 왼쪽아래 대각선과 max_number 비교
    if max_number < left_down:
        max_number = left_down

    print("#{} {}".format(tc, max_number))