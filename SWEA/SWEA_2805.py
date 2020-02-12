"""
농작물 수확하기
"""
# import sys
# sys.stdin = open("input.txt")

T = int(input())

for tc in range(T):
    N = int(input())
    Map = [list(map(int, input())) for _ in range(N)]
    sum = 0
    temp = 0
    for i in range((N//2)+1):
        for j in range((N//2) - temp, (N//2) + temp +1):
            sum += Map[i][j]
        temp += 1
    temp -= 2
    for i in range((N//2)+1, N):
        for j in range((N//2) - temp, (N//2) + temp +1):
            sum += Map[i][j]
        temp -= 1
    print("#{} {}".format(tc+1, sum))
