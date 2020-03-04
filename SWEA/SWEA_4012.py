"""
[모의 SW 역량테스트] 요리사
"""
from itertools import combinations
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

T = int(input())
for tc in range(T):
    N = int(input())
    Map = [list(map(int, input().split())) for _ in range(N)]
    comb = list(combinations(range(N), N//2))
    count = len(list(combinations(range(N), N//2)))//2
    temp = 0
    print("#{} {}".format(tc + 1, solve()))