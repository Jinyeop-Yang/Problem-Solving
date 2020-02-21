"""
빵집
"""
def dfs(y, x):
    global cnt
    visit[y][x] = 1
    if x == c - 1:
        # cnt += 1 이거 주석해체해주면 됨 vscode에서 에러 떠서 잠시 주석
        return 1
    for a, b in d:
        ny = y + a
        nx = x + b
        if 0 <= ny < r and Map[ny][nx] == '.' and not visit[ny][nx]:
            if dfs(ny,nx):
                return 1
    return
# 오른쪽 위 대각선, 오른쪽, 오른쪽 아래 대각선
d = [[-1, 1], [0, 1], [1, 1]]
r, c = map(int, input().split())
Map = [input() for _ in range(r)]
visit = [[0] * c for _ in range(r)]
cnt = 0

for i in range(r):
    dfs(i, 0)
print(cnt)