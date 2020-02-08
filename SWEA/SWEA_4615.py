"""
재미있는 오셀로 게임
"""
d = ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))
T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    Map = [[0] * (N + 1) for _ in range(N + 1)]
    Map[(N // 2)][(N // 2)] = Map[(N // 2) + 1][(N // 2) + 1] = 'W'
    Map[(N // 2)][(N // 2) + 1] = Map[(N // 2) + 1][(N // 2)] = 'B'
    b_cnt = w_cnt = 2
    put = []
    change = []
    for _ in range(M):
        put.append((list(map(int, input().split()))))

    for i in range(len(put)):
        y, x, color = put[i]
        if color == 1:
            color = 'B'
            b_cnt += 1
        else:
            color = 'W'
            w_cnt += 1

        for a, b in d:
            cnt = check = 0
            cy, cx = y, x
            while 1:
                ny, nx = cy + a, cx + b
                if ny < 1 or nx < 1 or N < ny or N < nx:
                    break
                if Map[ny][nx] == 0: break
                if Map[ny][nx] == color:
                    check = 1
                    break
                cnt += 1
                cy, cx = ny, nx
                change.append((ny,nx))
                
            if check == 0:
                change.clear()
                continue
            else:
                if check == 1 and cnt != 0:
                    if color == 'B':
                        Map[y][x] = 'B'
                        b_cnt += (len(change))
                        w_cnt -= (len(change))
                        for t_y, t_x in change:
                            Map[t_y][t_x] = 'B'
                    else:
                        Map[y][x] = 'W'
                        w_cnt += (len(change))
                        b_cnt -= (len(change))
                        for t_y, t_x in change:
                            Map[t_y][t_x] = 'W'
                    change.clear()

    print("#{} {} {}".format(tc + 1, b_cnt, w_cnt))