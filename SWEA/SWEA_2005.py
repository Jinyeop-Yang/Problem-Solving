#import sys
#sys.stdin = open("a.txt")

T = int(input())

for tc in range(T):
    N = int(input())

    a = [[0] * N for _ in range(N)]
    a[0][0] = 1
    for i in range(1, N):
        for j in range(N):
            if j == 0 or j == i:
                a[i][j] = 1
            if j > i: break
            else:
                a[i][j] = a[i-1][j-1] + a[i-1][j]

    print("#{}".format(tc+1))
    for i in range(N):
        for j in range(N):
            if a[i][j] != 0:
                print(a[i][j], end=' ')
        print()