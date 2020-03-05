"""
격자판의 숫자 이어 붙이기
"""
def dfs(y, x, cnt):
    if cnt == 7:
        res.add(''.join(map(str, temp)))
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < 4 and 0 <= nx < 4:
            temp.append(Map[ny][nx])
            dfs(ny, nx, cnt + 1)
            temp.pop()

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
T = int(input())
for tc in range(T):
    Map = [list(map(int, input().split())) for _ in range(4)]
    visit = [[0] * 4 for _ in range(4)]
    res = set()
    for i in range(4):
        for j in range(4):
            temp = []
            temp.append(Map[i][j])
            dfs(i, j, 1)
    print("#{} {}".format(tc + 1, len(res)))