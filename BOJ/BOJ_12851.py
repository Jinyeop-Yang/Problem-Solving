"""
숨바꼭질2
"""
from collections import deque

N, M = map(int, input().split())
res = max_n = 100001
visit = [0] * max_n
q = deque()
q.append((N, 0))
cnt = 0
while q:
    x, t = q.popleft()
    visit[x] = t
    if x == M:
        res = t if t < res else res
        cnt = cnt + 1 if t == res else cnt
    for nx in (x + 1, x - 1, x * 2):
        if 0 <= nx < max_n and not visit[nx]:
            q.append((nx, t + 1))
print(res, cnt, sep='\n')