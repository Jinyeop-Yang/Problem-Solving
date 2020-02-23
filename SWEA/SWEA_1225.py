"""
[S/W 문제해결 기본] 7일차 - 암호생성기
"""
from collections import deque

for _ in range(10):
    tc = int(input())
    lis = list(map(int, input().split()))
    q = deque()
    for i in lis:
        q.append(i)
    while 1:
        for i in range(1, 6):
            n = q.popleft()
            if n - i <= 0:
                q.append(0)
                break
            q.append(n - i)
        else:
            continue
        break
    print("#{} {}".format(tc, ' '.join(map(str, q))))