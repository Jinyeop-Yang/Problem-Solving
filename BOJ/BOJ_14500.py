"""
테트로미노
문제를 잘 읽자!
대칭도 되는건데 문제를 제대로 안읽음..
"""
N, M = map(int, input().split()) # N * M
Map = [list(map(int, input().split())) for _ in range(N)]
res = set()
for i in range(N):
    for j in range(M):
        # 1번
        if j + 3 < M:
            res.add(sum(Map[i][j:j+4]))
        if i + 3 < N:
            temp = 0
            for k in range(i, i + 4):
                temp += Map[k][j]
            res.add(temp)
        # 2번
        if i + 1 < N and j + 1 < M:
            res.add((Map[i][j] + Map[i][j+1] + Map[i+1][j] + Map[i+1][j+1]))
        # 3번
        if i + 2 < N and j + 1 < M:
            res.add((Map[i][j] + Map[i+1][j] + Map[i+2][j] + Map[i+2][j+1]))
            res.add((Map[i][j] + Map[i][j+1] + Map[i+1][j+1] + Map[i+2][j+1]))
            res.add((Map[i][j] + Map[i][j+1] + Map[i+1][j] + Map[i+2][j]))
        if i + 2 < N and j - 1 >= 0:
            res.add((Map[i][j] + Map[i+1][j] + Map[i+2][j] + Map[i+2][j-1]))
        if i + 1 < N and j + 2 < M:
            res.add((Map[i][j] + Map[i][j+1] + Map[i][j+2] + Map[i+1][j]))
            res.add((Map[i][j] + Map[i][j+1] + Map[i][j+2] + Map[i+1][j+2]))
            res.add((Map[i][j] + Map[i+1][j] + Map[i+1][j+1] + Map[i+1][j+2]))
        if i - 1 >= 0 and j + 2 < M:
            res.add((Map[i][j] + Map[i][j+1] + Map[i][j+2] + Map[i-1][j+2]))
        # 4번
        if i + 2 < N and j + 1 < M:
            res.add((Map[i][j] + Map[i+1][j] + Map[i+1][j+1] + Map[i+2][j+1]))
        if i + 2 < N and j - 1 >= 0:
            res.add((Map[i][j] + Map[i + 1][j] + Map[i + 1][j - 1] + Map[i + 2][j - 1]))
        if i - 1 >= 0 and j + 2 < M:
            res.add((Map[i][j] + Map[i][j+1] + Map[i-1][j+1] + Map[i-1][j+2]))
        if i + 1 < N and j + 2 < M:
            res.add((Map[i][j] + Map[i][j+1] + Map[i+1][j+1] + Map[i+1][j+2]))
        # 5번
        if i - 1 >= 0 and i + 1 < N and j + 1 < M:
            res.add((Map[i][j] + Map[i][j+1] + Map[i-1][j+1] + Map[i+1][j+1]))
            res.add((Map[i][j] + Map[i+1][j] + Map[i-1][j] + Map[i][j+1]))
        if i + 1 < N and j - 1 >= 0 and j + 1 < M:
            res.add((Map[i][j] + Map[i+1][j] + Map[i+1][j-1] + Map[i+1][j+1]))
            res.add((Map[i][j] + Map[i][j+1] + Map[i][j-1] + Map[i+1][j]))
print(max(res))