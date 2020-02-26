"""
로봇 청소기
사람들 너무 잘푼다.. 현타
"""
import sys
sys.stdin = open("input.txt")

def solve(y, x, dir):
    global res
    if not Map[y][x]:
        Map[y][x] = 2
        # res += 1 항상 글로벌쓰면 에러뜨더라
    for i in range(4):
        a, b = d[(dir + 3 - i) % 4]
        ny = y + a
        nx = x + b

        if 0 <= ny < N and 0 <= nx < M and not Map[ny][nx]:
            solve(ny,  nx, (dir + 3 - i) % 4)
    #4방향 다 청소 되어 있는 경우
    a, b = d[(dir+2) % 4]
    ny = y + a
    nx = x + b
    if Map[ny][nx] == 1:
        print(res); sys.exit(0)
    solve(ny, nx, dir)
# 0123 북동남서
d = [[-1, 0], [0, 1], [1, 0], [0, -1]]
N, M = map(int, input().split())
ry, rx, dir = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
res = 0
solve(ry, rx, dir)

"""
다른 풀이
d = [[-1, 0], [0, 1], [1, 0], [0, -1]]
N, M = map(int, input().split())
ry, rx, dir = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
res = 0
while 1:
    if not Map[ry][rx]:
        res += 1
        Map[ry][rx] = 2
    for i in range(1, 5):
        a, b = d[dir - i]
        ny, nx, D = ry + a, rx + b, (dir - i) % 4
        if not Map[ny][nx]:
            ry, rx, dir= ny, nx, D
            break
    else:
        # 4방향 다 청소 되어 있는 경우
        ry += d[(dir + 2) % 4][0]
        rx += d[(dir + 2) % 4][1]
        if Map[ry][rx] == 1:
            break
print(res)
"""

"""
import sys
sys.stdin = open("input.txt")
# 0123 북동남서
d = [[-1, 0], [0, 1], [1, 0], [0, -1]]
N, M = map(int, input().split())
ry, rx, dir = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
Map[ry][rx] = 2
res = 1
while 1:
    for i in range(4):
        a, b = d[(dir + 3 - i) % 4]
        ny, nx, D = ry + a, rx + b, (dir + 3 - i) % 4
        if not Map[ny][nx]:
            ry, rx, dir= ny, nx, D
            res += 1
            Map[ny][nx] = 2
            break
    else:
        # 4방향 다 청소 되어 있는 경우
        ny = ry + d[(dir + 2)%4][0]
        nx = rx + d[(dir + 2)%4][1]
        if Map[ny][nx] == 1:
            break
        ry, rx, D = ny, nx, dir
print(*Map, sep='\n')
print(res)
"""
