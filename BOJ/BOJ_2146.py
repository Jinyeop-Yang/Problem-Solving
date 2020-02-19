"""
다리 만들기
pypy vs python
재귀 최대 깊이 : pypy는 setrecusionlimit이 안먹힘
10000 vs 1000
"""
"""
dfs + bfs
"""
# import sys
# from collections import deque
# sys.setrecursionlimit(10**9)
# def bfs(y, x, n): #내가 아닌 다른 섬을 찾아가는 bfs
#     global res
#     visit[y][x] = 1
#     q = deque()
#     q.append((y, x, n, 0))

#     while q:
#         y, x, n, dist = q.popleft()
#         if Map[y][x] != 0 and Map[y][x] != n:
#             res = res if res < dist - 1 else dist - 1
#             break
#         for a, b in d:
#             ny = y + a
#             nx = x + b

#             if 0 <= ny < N and 0 <= nx < N and Map[ny][nx] != n and not visit[ny][nx]:
#                 visit[ny][nx] = 1
#                 q.append((ny, nx, n, dist + 1))

# def init(y, x, n): # 섬 labeling 해주는 dfs
#     Map[y][x] = n
#     for a, b in d:
#         ny = y + a
#         nx = x + b
#         if 0<= ny < N and 0<= nx < N and Map[ny][nx] == 1 and not visit[ny][nx]:
#             visit[ny][nx] = 1
#             init(ny, nx, n)

# d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
# N = int(input())
# Map = [list(map(int, input().split())) for _ in range(N)]
# visit = [[0] * N for _ in range(N)]
# temp = 1
# res = float('inf')

# for i in range(N):
#     for j in range(N):
#         if Map[i][j] == 1 and not visit[i][j]:
#             visit[i][j] = 1
#             init(i, j, temp)
#             temp += 1

# for i in range(N):
#     for j in range(N):
#         if Map[i][j] != 0:
#             for a, b in d:
#                 ny = i + a
#                 nx = j + b
#                 if 0 <= ny < N and 0 <= nx < N and Map[ny][nx] == 0:
#                     visit = [[0] * N for _ in range(N)]
#                     bfs(i, j, Map[i][j])
#                     break
# print(res)
"""
bfs + bfs
"""
import sys
from collections import deque
sys.stdin = open("input.txt")

def bfs(y, x, n):  # 내가 아닌 다른 섬을 찾아가는 bfs
    global res
    visit[y][x] = 1
    q = deque()
    q.append((y, x, n, 0))

    while q:
        y, x, n, dist = q.popleft()
        if Map[y][x] != 0 and Map[y][x] != n:
            res = res if res < dist - 1 else dist - 1
            break
        for a, b in d:
            ny = y + a
            nx = x + b

            if 0 <= ny < N and 0 <= nx < N and Map[ny][nx] != n and not visit[ny][nx]:
                visit[ny][nx] = 1
                q.append((ny, nx, n, dist + 1))


d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
temp = 1
res = float('inf')

for i in range(N):
    for j in range(N):
        if Map[i][j] == 1 and not visit[i][j]:
            q = deque()
            q.append((i, j))
            visit[i][j] = 1
            Map[i][j] = temp
            while q:
                y, x = q.popleft()
                for a, b in d:
                    ny = y + a
                    nx = x + b
                    if 0 <= ny < N and 0 <= nx < N and Map[ny][nx] == 1 and not visit[ny][nx]:
                        visit[ny][nx] = 1
                        Map[ny][nx] = temp
                        q.append((ny, nx))
            temp += 1

for i in range(N):
    for j in range(N):
        if Map[i][j] != 0:
            for a, b in d:
                ny = i + a
                nx = j + b
                if 0 <= ny < N and 0 <= nx < N and Map[ny][nx] == 0:
                    visit = [[0] * N for _ in range(N)]
                    bfs(i, j, Map[i][j])
                    break
print(res)