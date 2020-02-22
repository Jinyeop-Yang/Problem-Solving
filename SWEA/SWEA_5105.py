"""
[파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리
"""
from collections import deque

d= [[1, 0], [-1, 0], [0, -1], [0, 1]]
T = int(input())
for tc in range(T):
    N = int(input())
    Map = [list(map(int, input())) for _ in range(N)]
    visit = [[-1] * N for _ in range(N)]
    res = 0
    for i in range(N):
        for j in range(N):
            if Map[i][j] == 2:
                sy, sx = i, j
            elif Map[i][j] == 3:
                ey, ex = i, j
    q = deque()
    q.append((sy, sx))
    visit[sy][sx] = 0
    while q:
        y, x = q.popleft()
        if y == ey and x == ex:
            res = visit[y][x] - 1
            break
        for a, b in d:
            ny, nx = y + a, x + b

            if 0 <= ny < N and 0 <= nx < N and Map[ny][nx] != 1 and visit[ny][nx] == -1:
                visit[ny][nx] = visit[y][x] + 1
                q.append((ny, nx))
    print("#{} {}".format(tc + 1, res))