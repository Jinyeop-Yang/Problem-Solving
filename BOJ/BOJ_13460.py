from collections import deque
# import sys
# sys.stdin = open("input.txt")

def move(dir, y, x, hy, hx): # 각 방향으로 이동하면서 홀에 빠지는지 체크
    cnt = hole = 0
    if dir == 0: # 상
        while Map[y - cnt - 1][x] != '#':
            cnt += 1
            if y - cnt == hy and x == hx:
                hole = True
                break
        y -= cnt
    elif dir == 1: # 하
        while Map[y + cnt + 1][x] != '#':
            cnt += 1
            if y + cnt == hy and x == hx:
                hole = True
                break
        y += cnt

    elif dir == 2: # 좌
        while Map[y][x - cnt - 1] != '#':
            cnt += 1
            if x - cnt == hx and y == hy:
                hole = True
                break
        x -= cnt
    else: # 우
        while Map[y][x + cnt +1] != '#':
            cnt += 1
            if x + cnt == hx and y == hy:
                hole = True
                break
        x += cnt
    return hole, y, x, cnt

def compare_rb(dir, ry, rx, by, bx, res): # 같은 자리니까 더 많이 움직인 쪽이 멀리 있으니까 한칸 덜 오도록
    if dir == 0:
        if res: by += 1
        else: ry += 1
    elif dir == 1:
        if res: by -= 1
        else: ry -= 1
    elif dir == 2:
        if res: bx += 1
        else: rx += 1
    else:
        if res: bx -= 1
        else: rx -= 1
    return ry, rx, by, bx

def solve(cnt, d, ry, rx, by, bx, hy, hx): # red, blue, hole
    dq = deque()
    dq.append([cnt, d, ry, rx, by, bx, hy, hx])
    result = 0

    while dq:
        cnt, d, ry, rx, by, bx, hy, hx = dq.popleft()
        if cnt > 9:
            result = -1
            break
        for i in range(4): # 상하좌우 체크
            if cnt != 0: # 처음에는 상하좌우 다 돌아야 되기 때문에 거를 필요 없음
                if d == 0 or d == 1:
                    if i == 0 or i == 1: continue
                elif d == 2 or d == 3:
                    if i == 2 or i == 3: continue

            b_check, next_by, next_bx, b_cnt = move(i, by, bx, hy, hx)
            if b_check: # 파란색 공이 빠졌으면 진행할 필요없이 다음으로
                continue
            r_check, next_ry, next_rx, r_cnt = move(i, ry, rx, hy, hx)
            if r_check: # 빨간색 공이 빠졌으면 끝
                result = cnt + 1
                break
            if next_ry == next_by and next_rx == next_bx: # 옮겼을 때, 같은 위치면 이동
                next_ry, next_rx, next_by, next_bx = compare_rb(i, next_ry, next_rx, next_by, next_bx, b_cnt > r_cnt)
            
            dq.append([cnt + 1, i, next_ry, next_rx, next_by, next_bx, hy, hx])
        if result != 0:
            break
    return result

N, M = map(int, input().split())
Map = [input() for _ in range(N)]

for i in range(N):
    for j in range(M):
        if Map[i][j] == 'B':
            blue_y = i; blue_x = j
        if Map[i][j] == 'R':
            red_y = i; red_x = j
        if Map[i][j] == 'O':
            hole_y = i; hole_x = j

print(solve(0, None, red_y, red_x, blue_y, blue_x, hole_y, hole_x))
