"""
숨바꼭질
"""
# import sys
# sys.stdin= open("input.txt")
from collections import deque

N, M = map(int, input().split())
max_n = 100001
visit = [0] * max_n
q = deque()
q.append((N, 0))

while q:
    x, t = q.popleft()
    visit[x] = t
    if x == M:
        visit[x] = t; break
    for nx in (x + 1, x - 1, x * 2):
        if 0 <= nx < max_n and not visit[nx]:
            q.append((nx, t + 1))
print(visit[M])