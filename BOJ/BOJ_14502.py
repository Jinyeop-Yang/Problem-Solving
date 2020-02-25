"""
연구소
"""
from collections import deque
from itertools import combinations

def bfs(visit):
    cnt = len(comb) - 3
    q = deque()
    for i in virus:
        q.append(i)

    while q:
        y, x = q.popleft()
        for a, b in (-1, 0), (1, 0), (0, -1), (0, 1):
            ny = y + a
            nx = x + b

            if 0 <= ny < N and 0 <= nx < M:
                if not Map[ny][nx] and not visit[ny][nx]:
                    visit[ny][nx] = 1
                    q.append((ny, nx))
                    cnt -= 1
                    if cnt <= res: break
        else: continue
        break
    return cnt

N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
virus = []
comb = []
res = 0
for i in range(N):
    for j in range(M):
        if Map[i][j] == 2:
            virus.append([i, j])
        if not Map[i][j]:
            comb.append([i, j])
c = list(combinations(comb, 3))
for i in range(len(c)):
    visit = [[0] * M for _ in range(N)]
    for j in range(3):
        y, x = c[i][j][0], c[i][j][1]
        visit[y][x] = 1
    n = bfs(visit)
    res = res if res > n else n
print(res)