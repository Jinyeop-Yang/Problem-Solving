"""
스타트와 링크
combination 함수 이용해서 
"""
from itertools import combinations

N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]
comb = list(combinations(range(N), N//2))
count = len(list(combinations(range(N), N//2)))//2
temp = 0
def solve():
    res = float('inf')

    for l in range(count):
        a, b = 0, 0
        for i in range(N//2):
            for j in range(i+1, N//2):
                a += Map[comb[l][i]][comb[l][j]] + Map[comb[l][j]][comb[l][i]]
        for i in range(N//2):
            for j in range(i+1, N//2):
                b += Map[comb[count*2 -1 -l][i]][comb[count*2 -1 -l][j]] + Map[comb[count*2 -1 -l][j]][comb[count*2 -1 -l][i]]
        res = min(res, abs(a-b))

    return res
print(solve())

"""
조합 구현해서 실행
개선 -> 반만 실행하면 됨
N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]
visit = [0] * N
res = float('inf')
lis = []
lis1 = []
def solve():
    global res
    a, b = 0, 0

    for i in range(len(lis)):
        for j in range(i + 1, len(lis)):
            a += Map[lis[i]][lis[j]] + Map[lis[j]][lis[i]]
    for i in range(len(lis1)):
        for j in range(i + 1, len(lis1)):
            b += Map[lis1[i]][lis1[j]] + Map[lis1[j]][lis1[i]]
    res = min(res, abs(a-b))

def comb(idx, cnt):
    if cnt == N//2:
        for t in range(N):
            if not visit[t]:
                lis1.append(t)
        solve()
        lis1.clear()
        return
    for i in range(idx, N):
        if i not in lis and not visit[i]:
            lis.append(i)
            visit[i] = 1
            comb(i+1, cnt+1)
            lis.pop()
            visit[i] = 0
comb(0, 0)
print(res)
"""