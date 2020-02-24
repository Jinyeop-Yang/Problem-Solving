"""
[파이썬 S/W 문제해결 기본] 7일차 - 숫자 추가
"""
T = int(input())
for tc in range(T):
    N, M, L = map(int, input().split())
    lis = list(map(int, input().split()))
    for _ in range(M):
        lis.insert(*map(int, input().split()))
    print("#{} {}".format(tc + 1, lis[L]))