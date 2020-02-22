"""
공주님을 구해라!
"""
import sys
sys.stdin = open("input.txt")
from collections import deque

d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
N, M, T = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
res1 = res2 = float('inf')
q = deque()
q.append((0, 0, 0))
visit[0][0] = 1
while q:
    y, x, t = q.popleft()
    if y == N - 1 and x == M - 1:
        res2 = t if res2 > t else res2
    for a, b in d:
        ny = y + a
        nx = x + b

        if 0 <= ny < N and 0 <= nx < M and Map[ny][nx] != 1 and not visit[ny][nx]:
            visit[ny][nx] = t + 1
            if Map[ny][nx] == 2:
                res1 = t + 1 + (abs(ny - (N-1)) + abs(nx - (M - 1)))
            q.append((ny, nx, t + 1))
res = res1 if res1 < res2 else res2
if res <= T: print(res)
else: print('Fail')