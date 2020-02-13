"""
숫자 배열 회전
"""
T = int(input())

for tc in range(T):
    N = int(input())
    Map = [list(map(int, input().split())) for _ in range(N)]
    res = [[] for _ in range(N)]

    for i in range(N):
        for j in range(N-1,-1,-1):
            res[i].append(Map[j][i])
        res[i].append(' ')
        for j in range(N-1,-1,-1):
            res[i].append(Map[N-1-i][j])
        res[i].append(' ')
        for j in range(N):
            res[i].append(Map[j][N-1-i])
    print("#{}".format(tc+1))
    for i in range(N):
        print(''.join(map(str, res[i])))