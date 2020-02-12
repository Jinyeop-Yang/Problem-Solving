"""
섬의 개수
재귀 쓸려면 재귀깊이를 늘리자!
"""
# from collections import deque
# q = deque()
import sys
sys.setrecursionlimit(10**6)
# sys.stdin = open("input.txt")

d = [(1,0), (0,1), (-1,0),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]

def dfs(y, x):
    for a, b in d:
        ny = y + a
        nx = x + b
        if 0<= ny <N and 0<= nx <M:
            if Map[ny][nx] == 1 and visit[ny][nx] == 0:
                visit[ny][nx] = 1
                dfs(ny, nx)
    return
while True:
    M, N = map(int, input().split())
    if N==0 and M==0:
        break
    Map = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0]*M for _ in range(N)]
    island = 0

    for i in range(N):
        for j in range(M):
            if Map[i][j] == 1 and visit[i][j] == 0:
                island += 1
                visit[i][j] = 1
                dfs(i,j)
    print(island)