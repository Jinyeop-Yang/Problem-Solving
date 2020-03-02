"""
아맞다우산
순열로 간단하게 풀 수 있었다.
나는 내가 get한 X의 좌표를 가지고 다니면서 비교하면서 풀고 싶었는데
어케 구현할지 모르겠네..
"""
import sys
sys.stdin = open("input.txt")
from collections import deque
# from time import time
from itertools import permutations
# start = time()

def bfs(sy, sx, ey, ex, i):
    global res
    i.append((ey, ex))
    cnt = 0
    for iy, ix in i:
        if cnt >= res: break
        q = deque()
        q.append((sy, sx, 0)) # 시작 좌표
        visit = [[0] * N for _ in range(M)]
        visit[sy][sx] = 1
        while q:
            y, x, dist = q.popleft()
            if y == iy and x == ix:
                cnt += dist
                sy, sx = iy, ix
                break
            for temp in range(4):
                ny = y + dy[temp]
                nx = x + dx[temp]

                if 0 <= ny < M and 0 <= nx < N and Map[ny][nx] != '#' and not visit[ny][nx]:
                    visit[ny][nx] = 1
                    q.append((ny, nx, dist + 1))
        continue
    return cnt

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
N, M = map(int, input().split())
Map = [list(map(str, input())) for _ in range(M)]
item = []
sy = sx = ey = ex = 0
res = float('inf')
for i in range(M):
    for j in range(N):
        if Map[i][j] == 'S': # 시작 위치
            sy, sx = i, j
        elif Map[i][j] == 'E': # 끝 위치
            ey, ex = i, j
        elif Map[i][j] == 'X': # 챙겨야 할 물건 수
            item.append((i, j))

for i in permutations(item, len(item)):
    cnt = bfs(sy, sx, ey, ex, list(i))
    res = min(res, cnt)
print(res)
# print("{:.5}s".format(time() - start))