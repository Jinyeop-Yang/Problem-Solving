"""
어디에 단어가 들어갈 수 있을까
"""
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
                    if b == 1 :
                        if j-1 >= 0:
                            if Map[i][j-1] == 1: continue
                    else:
                        if i-1 >= 0:
                            if Map[i-1][j] == 1 : continue
                    if 0 <= i + a < N and 0 <= j + b < N:
                        temp = 1
                        t_y = i; t_x= j
                        while Map[t_y][t_x] != 0:
                            ny = t_y + a
                            nx = t_x + b
                            if Map[ny][nx] == 1:
                                temp += 1
                            t_y = ny; t_x = nx
                            if b == 0 :
                                if ny == N-1: break
                            else:
                                if nx == N-1: break
                        if temp == K:
                            cnt += 1

    print("#{} {}".format(tc+1, cnt))