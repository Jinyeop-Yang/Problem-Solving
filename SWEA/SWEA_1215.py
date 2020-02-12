"""
[S/W 문제해결 기본] 3일차 - 회문1
"""
# import sys
# sys.stdin = open("input.txt", "r")

for tc in range(10):
    M = int(input())
    MAP = [input() for _ in range(8)]
    cnt = 0
    # 행에서 회문 찾기
    for i in range(8):
        for j in range(8 - M + 1):
            if MAP[i][j:M + j] == ''.join(reversed(MAP[i][j:M + j])): # MAP[i][::-1] 이거도 거꾸로 출력 가능
                cnt += 1
    # 열에서 회문 찾기
    for i in range(8):
        for j in range(8 - M + 1):
            string = ''
            for k in range(j, j + M):
                string += MAP[k][i]
            if string == string[::-1]:
                cnt += 1

    print('#{} {}'.format(tc + 1, cnt))