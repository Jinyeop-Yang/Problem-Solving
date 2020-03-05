"""
[모의 SW 역량테스트] 벌꿀채취
max_h 함수만 구현하면 쉽게 푸는건데
combinations 안쓸라고 하다가 오래걸림.. 걍 써버림 ㅎ
"""
from itertools import combinations

def max_h(select):
    a = 0
    for i in range(1, M + 1):
        for j in combinations(select, i):
            if sum(j) <= C:
                t = 0
                for e in j:
                    t += e ** 2
                a = t if t > a else a
    return a

def solve(y, x):
    global res, temp
    for i in range(y, N):
        if i != y:
            x = 0
        for j in range(x, N - M + 1):
            if not visit[i][j]:
                select = honey[i][j: j + M]
                if len(select) == M:
                    temp1 = max_h(select)
                    res = max(res, temp + temp1)

T = int(input())
for tc in range(T):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    res = float('-inf')
    for i in range(N):
        for j in range(N - M + 1):
            select = honey[i][j: j + M]
            for k in range(j, j + M):
                visit[i][k] = 1
            temp = max_h(select)
            solve(i, j)
            for k in range(j, j + M):
                visit[i][k] = 0

    print("#{} {}".format(tc + 1, res))