"""
알파벳
dy, dx 따로 선언해주고
입력도 이제 라인으로 받자. 그게 시간적으로 이득이다.
+ 초기값은 선언하면서 넣어주는게 시간적으로 이득이다.
1등 코드 참고해서 공부해두자.
string 배열을 만들어서 비교했음 완전 천재다.

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
cache = [['' for _ in range(C)] for _ in range(R)]
def bfs(x, y):
    queue = [(x, y, board[x][y])]
    ans = 0
    while queue:
        x, y, path = queue.pop()
        chk = False
        for i, j in (1, 0), (-1, 0), (0, 1), (0, -1):
            xx, yy = x+i, y+j
            if xx < 0 or yy < 0 or xx >= R or yy >= C:
                continue
            if board[xx][yy] not in path:
                chk = True
                if cache[xx][yy] != path + board[xx][yy]:
                    cache[xx][yy] = path + board[xx][yy]
                    queue.append((xx, yy, path + board[xx][yy]))
        if not chk:
            ans = max(ans, len(path))
    return ans
print(bfs(0, 0))

"""
import sys
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]
def bfs(y, x):
    global cnt
    q = set([(y, x, Map[y][x])])
    while q:
        y, x, s = q.pop()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < r and 0 <= nx < c and Map[ny][nx] not in s:
                q.add((ny, nx, s+Map[ny][nx]))
                cnt = max(cnt, len(s) + 1)

r, c = map(int, sys.stdin.readline().split())
Map = [list(sys.stdin.readline().strip()) for _ in range(r)]
cnt = 1
bfs(0,0)
print(cnt)