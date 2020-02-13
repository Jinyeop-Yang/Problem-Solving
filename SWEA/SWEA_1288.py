"""
새로운 불면증 치료법
"""
# import sys
# sys.stdin = open("input.txt")
T = int(input())
for tc in range(T):
    flag = 0
    t = 1
    lis = []
    N = int(input())
    while 1:
        n = N * t
        t += 1
        while n > 0:
            temp = n % 10
            if temp not in lis:
                lis.append(temp)
            if len(lis) == 10:
                flag = 1; break
            n //= 10
        if flag == 1: break
    print("#{} {}".format(tc+1, N*(t-1)))