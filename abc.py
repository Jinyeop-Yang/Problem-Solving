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
d= ((1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1))

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    Map = [[0]*(N+1) for _ in range(N+1)]
    Map[(N//2)][(N//2)] = Map[(N//2)+1][(N//2)+1] = 'W'
    Map[(N//2)][(N//2)+1] = Map[(N//2)+1][(N//2)] = 'B'
    b_cnt = w_cnt = 2
    put = []
    # for i in range(N+1):
    #     print(Map[i])
    for _ in range(M):
        put.append((list(map(int, input().split()))))

    for i in range(len(put)):
        y, x, color = put[i]
        if color == 1 : color = 'B'
        else: color = 'W'
        # 1이면 B, 2이면 W
        # 놓고 나서 0이 아닐때 까지 카운트 & 범위 확인
        # 카운트가 2 이상일때 빼기빼기하면서 원래자리 오면서
        # 다른거 있으면 바꾸고 b_cnt w_cnt 업데이트
        # 놓을때마다 대각선 상하좌우 다 살펴야함.
        # 다른거 있을때만 놓을 수 있다.
        # 못놓으면 다음 사람한테 간다.
        for a, b in d:
            # print(a, b)
            cnt = 0
            cy, cx = y, x
            while 1:
                ny, nx = cy + a, cx + b
                # print(ny, nx)
                # print('------')
                if ny<1 or nx<1 or N<ny or N<nx:
                    break
                if Map[ny][nx] == color or Map[ny][nx] == 0:
                    break
                cnt += 1
                cy, cx = ny, nx
                if color == 'B' : Map[ny][nx] = 'W'
                else: Map[ny][nx] = 'B'

            if cnt == 0:
                continue
            else:
                if color == 'B':
                    Map[y][x] = 'B'
                    b_cnt += cnt; w_cnt -= cnt
                else:
                    Map[y][x] = 'W'
                    w_cnt += cnt
                    b_cnt -= cnt
            
    print("#{} {} {}".format(tc+1, b_cnt, w_cnt))