"""
[파이썬 S/W 문제해결 기본] 4일차 - 종이붙이기
"""
def dfs(n):
    if n > N: return 0
    if n == N:
        return 1
    return dfs(n + 10) + dfs(n + 20) * 2

T = int(input())
for tc in range(T):
    N = int(input())
    print("#{} {}".format(tc+1, dfs(0)))