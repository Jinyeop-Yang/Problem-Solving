"""
[파이썬 S/W 문제해결 기본] 5일차 - 미로
"""
d = [[-1,0],[1,0],[0,-1],[0,1]]
def dfs(y, x):
    global res
    visit[y][x] = 1
    #if not res: 이거 왜 안되지
    for a, b in d:
        ny = y + a
        nx = x + b
        if 0<= ny < N and 0 <= nx < N and Map[ny][nx] != 1 and not visit[ny][nx] and not res:
            if Map[ny][nx] == 3:
                res = 1; return
            dfs(ny,nx)

T = int(input())
for tc in range(T):
    N = int(input())
    Map = [list(map(int, input())) for _ in range(N)]
    visit = [[0]*N for _ in range(N)]
    res = flag = 0
    for i in range(N):
        for j in range(N):
            if Map[i][j]==2:
                dfs(i,j)
                flag = 1; break
        if flag: break

    print("#{} {}".format(tc+1, res))