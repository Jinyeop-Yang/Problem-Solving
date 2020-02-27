"""
장훈이의 높은 선반
dfs다. 참고했음
"""
def dfs(idx, sum):
    global res
    if sum >= B:
        res = min(res, sum)
    if idx == N:
        return
    dfs(idx + 1, sum + numbers[idx])
    dfs(idx + 1, sum)

T = int(input())
for tc in range(T):
    N, B = map(int, input().split())
    numbers = list(map(int, input().split()))
    res = float('inf')
    dfs(0, 0)
    print("#{} {}".format(tc+1, res - B))