"""
[S/W 문제해결 기본] 7일차 - 미로2
"""
from collections import deque
d = [[-1,0],[1,0],[0,-1],[0,1]]

for tc in range(10):
    t = int(input())
    res = 0
    Map = [list(map(int, input())) for _ in range(100)]
    visit = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if Map[i][j] == 2:
                sy, sx = i, j
            elif Map[i][j] == 3:
                ey, ex = i, j
    visit[sy][sx] = True
    q = deque()
    q.append((sy, sx))
    while q:
        y, x = q.popleft()
        if y == ey and x == ex:
            res = 1; break
        for a, b in d:
            ny = y + a
            nx = x + b

            if 0 <= ny < 100 and 0 <= nx < 100 and not res and Map[ny][nx] != 1 and not visit[ny][nx]:
                visit[ny][nx] = 1
                q.append((ny, nx))

    print("#{} {}".format(t, res))