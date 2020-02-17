"""
숨바꼭질3
*2, -1, +1의 순서로 돌아야함 / 4 6의 경우 답은 1
다익스트라라고 한다.
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
        break
    for nx in (x * 2, x - 1, x + 1):
        if 0 <= nx < max_n and not visit[nx]:
            if nx == x * 2:
                q.append((nx, t))
            else:
                q.append((nx, t + 1))
print(visit[M])