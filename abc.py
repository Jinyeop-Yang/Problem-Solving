# s = [1,2,3,4,5]
# a = []
# def dfs(idx, cnt):
#     if cnt == 5:
#         print(a)
#         return
    
#     for i in range(0, len(s)):
#         a.append(s[i])
#         dfs(i, cnt+1)
#         a.pop()

# dfs(0,0)
import sys
sys.stdin = open("input.txt")
d = [(1,0),(0,1)]

T = int(input())

for tc in range(T):
    N , K = map(int, input().split())
    Map = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if Map[i][j] == 1:
                for a, b in d:
                    temp = 1
                    if 0 <= i + a < N and 0 <= j + b < N:
                        while 1:
                            ny = i + a
                            nx = j + b
                            if Map[ny][nx] == 1:
                                temp += 1
                                if ny == N-1 or nx == N-1:
                                    break
                        if temp == K:
                            cnt += 1

    print("#{} {}".format(tc+1, cnt))


    