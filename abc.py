# s = [1,2,3,4,5]
# a = []
# def dfs(idx, cnt):
#     if cnt == 3:
#         print(a)
#         return
    
#     for i in range(0, len(s)):
#         a.append(s[i])
#         dfs(i, cnt+1)
#         a.pop()
# dfs(0,0)
# import sys
# sys.stdin = open("input.txt")
# sys.setrecursionlimit(10**6)

T = int(input())
for tc in range(T):
    cnt = 0
    t = 1
    lis = []
    N = int(input())
    while 1:
        t += 1
        while N>0:
            temp = N % 10
            if temp not in lis:
                lis.append(temp)
            N //= 10
            cnt += 1
        if len(lis) == 10: break
        N *= t
    print("#{} {}".format(tc+1, cnt))