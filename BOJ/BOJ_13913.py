"""
숨바꼭질4
"""
from collections import deque

N, M = map(int, input().split())
max_n = 100001
visit = [-1] * max_n
q = deque()
q.append((N, 0))
visit[N] = N
while q:
    x, t = q.popleft()
    if x == M:
        route = [x]
        while x != N:
            route.append(visit[x])
            x = visit[x]
        print(t)
        print(*reversed(route))
    for nx in (x * 2, x - 1, x + 1):
        if 0 <= nx < max_n and visit[nx] == -1:
            q.append((nx, t + 1))
            visit[nx] = x