"""
[S/W 문제해결 기본] 4일차 - 거듭 제곱
"""
def dfs(a):
    if a == 1:
        return n
    return n * dfs(a - 1)

for _ in range(10):
    tc = int(input())
    n, a = map(int, input().split())
    print("#{} {}".format(tc, dfs(a)))