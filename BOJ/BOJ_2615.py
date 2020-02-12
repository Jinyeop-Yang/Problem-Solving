"""
오목
"""
# import sys
# sys.stdin = open("input.txt")

d = [[1,0],[0,1],[-1,1],[1,1]]
# 8방향 다 봐줬었는데 오른쪽으로 탐색하니까 오른쪽 방향 4개만 봐줘도 됨
def find(n, y, x):
    for a, b in d:
        ny = y + a
        nx = x + b
        if nx < 0 or ny < 0 or 19 <= nx or 19 <= ny: continue
        if Map[ny][nx] != n: continue
        cnt = 1
        while Map[ny][nx] == n:
            cnt += 1
            ny += a; nx += b
            if nx < 0 or ny < 0 or 19 <= nx or 19 <= ny: break
        if cnt == 5:
            return True, a, b
    return 0, 0, 0

flag = 0
Map = [list(map(int, input().split())) for _ in range(19)]
for i in range(19):
    for j in range(19):
        if Map[i][j] != 0:
            res, a, b = find(Map[i][j], i, j)
            if res:
                if Map[i-a][j-b] == Map[i][j]: continue
                if b < 0:
                    print(Map[i][j])
                    print(i + (a * 4)+1 , j + (b * 4) + 1)
                else:
                    print(Map[i][j])
                    print(i+1, j+1)
                flag = 1
                break
    if flag: break
if not flag: print(0)