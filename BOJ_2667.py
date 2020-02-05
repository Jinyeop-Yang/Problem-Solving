from collections import deque

N = int(input())
Map = [input() for _ in range(N)]
visit = [[0] * N for _ in range(N)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
q = deque()
danji = 0
danji_list = []

for i in range(N):
    for j in range(N):
        if Map[i][j] == 1 and visit[i][j] == 0:
            danji += 1
            q.append([i,j])
            visit[i][j] = 1
            sum = 1
            while q:
                y, x = q.pop()
                for a, b in d:
                    ny = y + a
                    nx = x + b
                    if 0 <= y < N and 0 <= x < N and visit[ny][nx] == 0:
                        sum += 1
                        q.append(ny,nx)
                        visit[ny][nx] = 1
            danji_list.append(sum)
danji_list.sort()
print(danji)
for i in danji_list:
    print(i)