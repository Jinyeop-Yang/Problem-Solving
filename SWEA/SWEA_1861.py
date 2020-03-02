"""
정사각형 방

늘 중복제거가 핵심
"""
from collections import deque

def bfs(y, x):
    q = deque()
    q. append((y, x))
    t = 0
    n = float('inf')
    while q:
        y, x = q.popleft()
        n = min(n, Map[y][x])
        for a in range(4):
            ny = y + dy[a]
            nx = x + dx[a]

            if 0 <= ny < N and 0 <= nx < N and abs(Map[y][x] - Map[ny][nx]) == 1 and not visit[ny][nx]:
                visit[ny][nx] = 1
                visit1[ny][nx] = 1
                t += 1
                q.append((ny, nx))

    return t, n

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
T = int(input())
for tc in range(T):
    N = int(input())
    Map = [list(map(int, input().split())) for _ in range(N)]
    visit1 = [[0] * N for _ in range(N)]

    num, cnt = float('inf'), 0
    for i in range(N):
        for j in range(N):
            if not visit1[i][j]:
                visit = [[0] * N for _ in range(N)]
                visit[i][j] = 1
                temp, n = bfs(i, j)
                if temp >= cnt:
                    if cnt == temp:
                        num = num if num < n else n
                    else:
                        num = n
                    cnt = temp
    print("#{} {} {}".format(tc + 1, num, cnt + 1))