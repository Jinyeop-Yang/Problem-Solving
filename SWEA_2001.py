def my_sum(i, j, m):
    hap = 0
    for a in range(i, m+i):
        for b in range(j, m+j):
           hap += Map[a][b]
    return hap 

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    Map = [list(map(int, input().split())) for _ in range(N)]
    sum = temp = 0
    
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = my_sum(i,j, M)
            if sum < temp:
                sum = temp

    print("#{} {}".format(tc + 1, sum))