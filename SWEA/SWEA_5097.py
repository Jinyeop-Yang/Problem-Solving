"""
[파이썬 S/W 문제해결 기본] 6일차 - 회전
"""
from collections import deque

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    q = deque()
    lis = list((map(int,input().split())))
    for i in lis:
        q.append(i)
    for i in range(M % len(lis)):
        a = q.popleft()
        q.append(a)

    print("#{} {}".format(tc+1, q[0]))