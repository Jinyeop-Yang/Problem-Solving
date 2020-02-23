"""
[파이썬 S/W 문제해결 기본] 6일차 - 피자 굽기
"""
from collections import deque

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    lis = list(map(int, input().split()))
    lis1 = []
    for i, j in enumerate(lis):
        lis1.append((i,j))
    res = 0
    q = deque()
    for i in range(N):
        q.append(lis1.pop(0))
    while len(q) != 1:
        while len(q) != N and lis1:
            q.append(lis1.pop(0))
        idx, temp = q.popleft()
        if temp // 2 == 0: continue
        else:
            q.append((idx, temp//2))
    res = q[0][0]
    print("#{} {}".format(tc + 1, res + 1))