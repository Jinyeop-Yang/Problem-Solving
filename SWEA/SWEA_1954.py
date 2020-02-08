"""
달팽이 숫자
"""
# import sys
# sys.stdin = open("input.txt")

T = int(input())

for tc in range(T):
    N = int(input())
    print("#{}".format(tc+1))
    start = 1
    Map = [[0]*N for _ in range(N)]
    y = x = 0
    Map[y][x] = 1

    while start< N*N:
        while x < N - 1:
            x += 1
            if Map[y][x] != 0:
                x -= 1; break
            start += 1
            Map[y][x] = start
        while y < N - 1:
            y += 1
            if Map[y][x] != 0:
                y -= 1; break
            start += 1
            Map[y][x] = start
        while x > 0:
            x -= 1
            if Map[y][x] != 0:
                x += 1; break
            start += 1
            Map[y][x] = start
        while y > 0:
            y -= 1
            if Map[y][x] != 0:
                y += 1; break
            start += 1
            Map[y][x] = start

    for i in range(N):
        print(*Map[i])