"""
[파이썬 S/W 문제해결 기본] 4일차 - 그래프 경로
"""
def dfs(n):
    global res, end
    if n == end:
        res = 1; return
    if not res:
        for i in range(v+1):
            if Map[n][i] == 1 and not visit[i] and not res:
                visit[n] = 1; dfs(i)

T = int(input())
for tc in range(T):
    res = 0
    v, e = map(int, input().split())
    Map = [[0]* (v+1) for _ in range(v+1)]
    visit = [0] * (v+1)
    for _ in range(e):
        a, b  = map(int, input().split())
        Map[a][b] = 1
    start, end = map(int, input().split())
    visit[start] = 1
    dfs(start)
    print("#{} {}".format(tc+1, res))