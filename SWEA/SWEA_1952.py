"""
[모의 SW 역량테스트] 수영장
a형에서 readline 못쓰는거같음..
걍 원래대로 input으로
"""
import sys
sys.stdin = open("input.txt")

def dfs(idx, sum):
    global min_fee
    if idx >= len(lis):
        min_fee = min(min_fee, sum)
        return

    dfs(idx + 1, sum + lis[idx] * d) # 하루치 등록
    dfs(idx + 1, sum + o) # 한달치 등록
    dfs(idx + 3, sum + t) # 세달치 등록

T = int(input())
for tc in range(T):
    d, o, t, y = map(int, sys.stdin.readline().split())
    month = list(map(int, sys.stdin.readline().split()))
    lis = []
    for i in range(12):
        if month[i]: lis.append(month[i])
    min_fee = y
    dfs(0, 0) # idx랑 합계를 같이 보낸다.

    print("#{} {}".format(tc + 1, min_fee))