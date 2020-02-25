"""
레이저 통신
같은 방향이면 안늘리고 다른 방향이면 +1 해주는거 까지 ok
끝까지 가야된다는 생각을 못했음.
그리고 break거는 if문에 좌표를 or로 해줘야 했다.
"""
from collections import deque
dy , dx = [-1, 1, 0, 0], [0, 0, -1, 1]
W, H = map(int, input().split())
Map = [input() for _ in range(H)]
visit = [[0] * W for _ in range(H)]
q = deque()
for i in range(H):
    for j in range(W):
        if Map[i][j] == 'C':
            q.append((i, j))
            sy, sx = i, j
            break
    else: continue
    break
while q:
    y, x = q.popleft()
    if (y != sy or x != sx) and Map[y][x] == 'C':
        print(visit[y][x] - 1); break
    for a in range(4):
        ny = y + dy[a]
        nx = x + dx[a]

        while 0 <= ny < H and 0 <= nx < W and Map[ny][nx] != '*':
            if not visit[ny][nx]:
                q.append((ny, nx))
                visit[ny][nx] = visit[y][x] + 1
            ny += dy[a]
            nx += dx[a]