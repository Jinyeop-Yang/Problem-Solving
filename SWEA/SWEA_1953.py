"""
[모의 SW 역량테스트] 탈주범 검거

다음 칸을 갈때 -해서 반대방향의 입구가 있는지 확인하면
더 짧게 짤 수 있다.
"""
from collections import deque

def bfs(y, x):
    cnt = 1
    q = deque()
    q.append((y, x, 1))
    visit[y][x] = 1
    while q:
        y, x, t = q.popleft()
        d = []
        if t >= L:
            break
        if Map[y][x] == 1:
            for i in range(4):
                d.append(i)
        elif Map[y][x] == 2:
            d.append(0); d.append(1)
        elif Map[y][x] == 3:
            d.append(2); d.append(3)
        elif Map[y][x] == 4:
            d.append(0); d.append(3)
        elif Map[y][x] == 5:
            d.append(1); d.append(3)
        elif Map[y][x] == 6:
            d.append(1); d.append(2)
        elif Map[y][x] == 7:
            d.append(0); d.append(2)
        for a in d:
            ny = y + dy[a]
            nx = x + dx[a]
            
            if 0 <= ny < N and 0 <= nx < M and Map[ny][nx] != 0 and not visit[ny][nx]:
                if a == 0:
                    if Map[ny][nx] == 3 or Map[ny][nx] == 4 or Map[ny][nx] == 7: continue
                elif a == 1:
                    if Map[ny][nx] == 3 or Map[ny][nx] == 5 or Map[ny][nx] == 6: continue
                elif a == 2:
                    if Map[ny][nx] == 2 or Map[ny][nx] == 6 or Map[ny][nx] == 7: continue
                elif a == 3:
                    if Map[ny][nx] == 2 or Map[ny][nx] == 4 or Map[ny][nx] == 5: continue

                visit[ny][nx] = 1
                cnt += 1
                q.append((ny, nx, t + 1))

    return cnt

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
T = int(input())
for tc in range(T):
    N, M, R, C, L = map(int, input().split())
    Map = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * M for _ in range(N)]
    print("#{} {}".format(tc+1, bfs(R, C)))