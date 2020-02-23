"""
[파이썬 S/W 문제해결 기본] 6일차 - 노드의 거리
"""
from collections import deque

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    lis = [list(map(int, input().split())) for _ in range(E + 1)]
    lis1 = []
    S, G = lis.pop()
    res = 0
    q = deque()
    for i in range(len(lis)):
        if lis[i][0] == S:
            q.append((lis[i][1], 1))
            lis1.append(i)
        elif lis[i][1] == S:
            q.append((lis[i][0], 1))
            lis1.append(i)
    while q:
        s, c = q.popleft()
        if s == G:
            res = c; break
        for i in range(len(lis)):
            if i not in lis1 and lis[i][0] == s:
                q.append((lis[i][1], c + 1))
                lis1.append(i)
            elif i not in lis1 and lis[i][1] == s:
                q.append((lis[i][0], c + 1))
                lis1.append(i)

    print("#{} {}".format(tc + 1, res))