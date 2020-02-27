"""
[S/W 문제해결 응용] 7일차 - 행렬찾기
"""
def solve(y,x):
    cnt = 0
    while Map[y+cnt][x]:
        cnt += 1
        if y + cnt == N: break
    cnt1 = 0
    while Map[y][x+cnt1]:
        cnt1 += 1
        if x + cnt1 == N: break
    for i in range(y, y+cnt):
        for j in range(x, x+cnt1):
            visit[i][j] = 1

    if not res:
        res.extend([cnt, cnt1])
    else:
        for i in range(0, len(res), 2):
            if res[i] * res[i+1] > cnt * cnt1:
                res.insert(i, cnt)
                res.insert(i + 1, cnt1)
                break
            elif res[i] * res[i + 1] == cnt * cnt1:
                if res[i] > cnt:
                    res.insert(i, cnt)
                    res.insert(i+1, cnt1)
                else:
                    res.insert(i+2, cnt)
                    res.insert(i+3, cnt1)
                break
        else:
            res.extend([cnt, cnt1])

T = int(input())
for tc in range(T):
    N = int(input())
    Map = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    res = []
    for i in range(N):
        for j in range(N):
            if Map[i][j] and not visit[i][j]:
                solve(i, j)

    print("#{} {} {}".format(tc + 1, len(res) // 2, ' '.join(map(str, res))))