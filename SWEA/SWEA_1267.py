"""
[S/W 문제해결 응용] 10일차 - 작업순서
"""
def dfs(n):
    for i in range(1, v+1):
        if Map[n][i] == 1:
            cnt = 0
            for a in range(1, v+1):
                if a != n:
                    if Map[a][i] == 1:
                        cnt += 1
            if not cnt:
                lis.append(i)
                Map[n][i] = 0
                dfs(i)
            else:
                Map[n][i] = 0

for tc in range(10):
    v, e = map(int,input().split())
    Map = [[0] * (v+1) for _ in range(v+1)]
    temp = list(map(int,input().split()))
    lis = []
    for i in range(0, len(temp), 2):
        Map[temp[i]][temp[i+1]] = 1
    for i in range(1, v+1):
        cnt = 0
        for j in range(1, v+1):
            if Map[j][i] == 1:
                cnt += 1
        if not cnt:
            if i not in lis:
                lis.append(i)
                dfs(i)
    print("#{}".format(tc+1), end=' ')
    print(*lis)