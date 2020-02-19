"""
상범빌딩
"""
import sys
sys.stdin = open("input.txt")
from collections import deque

# 위층, 아래층, 상 하 좌 우
d = [[-1, 0, 0], [1, 0, 0], [0, -1 , 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]
while 1:
    L, R, C = map(int, input().split())
    if not L and not R and not C: break
    Map = [[input() for _ in range(R+1)] for _ in range(L)]
    for i in range(L):
        Map[i].pop()
    visit = [[[0] * C for _ in range(R)] for _ in range(L)]
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if Map[i][j][k] == 'S':
                    sfloor, sy, sx = i, j, k
                if Map[i][j][k] == 'E':
                    efloor, ey, ex = i, j, k

    q = deque()
    time = 0
    q.append((sfloor, sy, sx, time))
    visit[sfloor][sy][sx] = 1
    while q:
        f, y, x, t = q.popleft()
        if f == efloor and y == ey and x == ex:
            print('Escaped in {} minute(s).'.format(t))
            break
        for a, b, c in d:
            nf = f + a
            ny = y + b
            nx = x + c

            if 0 <= nf < L and 0 <= ny < R and 0 <= nx < C and Map[nf][ny][nx] != '#' and not visit[nf][ny][nx]:
                visit[nf][ny][nx] = 1
                q.append((nf, ny, nx, t + 1))
    else:
        print('Trapped!')