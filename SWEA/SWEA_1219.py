"""
[S/W 문제해결 기본] 4일차 - 길찾기
"""
from collections import deque

for _ in range(10):
    tc, l = map(int, input().split())
    lis = list(map(int, input().split()))
    res = 0
    q = deque()
    for i in range(0, len(lis), 2):
        if lis[i] == 0: q.append((lis[i], lis[i + 1]))
    while q:
        cn, nn = q.popleft()
        if nn == 99: res = 1; break
        for i in range(0, len(lis), 2):
            if lis[i] == nn: q.append((lis[i], lis[i + 1]))

    print("#{} {}".format(tc, res))