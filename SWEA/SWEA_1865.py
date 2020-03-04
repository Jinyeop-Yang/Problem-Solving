"""
동철이의 일 분배
"""
import sys
sys.stdin = open("input.txt")

def dfs(r):
    global temp, res
    if temp <= res:
        return
    if r == N:
        res = temp; return

    for i in range(N):
        if not visit[i]:
            if not Map[r][i]: continue
            else:
                visit[i] = 1
                temp *= (Map[r][i]/100)
                dfs(r + 1)
                temp /= (Map[r][i]/100)
                visit[i] = 0

T = int(input())
for tc in range(T):
    N = int(input())
    Map = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N
    temp, res = 1, float('-inf')

    dfs(0)

    print("#{} {:.6f}".format(tc + 1, res * 100))