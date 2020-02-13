"""
[S/W 문제해결 기본] 7일차 - 미로1
"""
# import sys
# sys.stdin = open("input.txt")

d = [[-1,0],[1,0],[0,-1],[0,1]]

def dfs(y, x):
    if Map[y][x] == 3:
        global res
        res = 1; return

    if not res:
        for a, b in d:
            ny = y + a
            nx = x + b

            if 0 <= ny < 16 and 0 <= nx < 16 and not res and Map[ny][nx] != 1 and not visit[ny][nx]:
                visit[ny][nx] = 1
                dfs(ny, nx)
                visit[ny][nx] = 0

for tc in range(10):
    t = int(input())
    res = 0
    Map = [list(map(int, input())) for _ in range(16)]
    visit = [[0 for _ in range(16)] for _ in range(16)]
    visit[1][1] = True
    dfs(1,1)
    print("#{} {}".format(t, res))