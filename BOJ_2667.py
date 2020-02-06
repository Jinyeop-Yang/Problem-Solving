from collections import deque
N = int(input())
Map = [list(map(int, input())) for _ in range(N)]
visit = [[0]*N for _ in range(N)]
d = [(1,0), (-1,0), (0,1), (0,-1)]
q = deque()
danji = []
for i in range(N):
    for j in range(N):
        if Map[i][j] == 1 and visit[i][j] == 0:
            visit[i][j] = 1
            q.append((i,j))
            cnt = 1
            while q:
                y, x = q.pop()
                for a, b in d:
                    ny = y + a
                    nx = x + b
                    if ny<0 or nx<0 or N<=ny or N<=nx:
                        continue
                    if visit[ny][nx] == 1 or Map[ny][nx] == 0:
                        continue
                    visit[ny][nx] = 1
                    cnt += 1
                    q.append((ny, nx))
            danji.append(cnt)
print(len(danji))
danji.sort()
for i in range(len(danji)):
    print(danji[i])