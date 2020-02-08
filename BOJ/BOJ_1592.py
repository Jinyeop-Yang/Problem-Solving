"""
영식이와 친구들
"""
import sys
sys.stdin = open("input.txt")
N, M, L = map(int, input().split())
lis = [0]*(N)
cnt = 0
idx = lis[1] = 1

while lis[idx] != M:
    if lis[idx] % 2:
        lis[(((idx-L)+N) % N)] += 1
        cnt += 1
        idx = (((idx-L)+N) % N)
    else:
        lis[(((idx+L)+N) % N)] += 1
        cnt += 1
        idx = (((idx+L)+N) % N)
print(cnt)