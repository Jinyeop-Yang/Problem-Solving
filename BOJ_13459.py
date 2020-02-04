import sys
from collections import deque

sys.stdin = open("input.txt")
def move(dir, y, x, hy, hx): # 각 방향으로 이동하면서 홀에 빠지는지 체크
    if dir == 0 : # 상
    elif dir == 1: # 하
    elif dir == 2: # 좌
    else: # 우
    return hole, y, x, cnt

def compare_rb(dir, ry, rx, by, bx, res): # 같은 자리니까 이동
    if dir == 0:
        if res: by -= 1
        else: ry -= 1
    elif dir == 1:
        if res: by += 1
        else: ry += 1
    elif dir == 2:
        if res: bx += 1
        else: rx += 1
    else:
        if res: bx -= 1
        else: rx -= 1
    return ry, rx, by, bx

def solve(cnt, ry, rx, by, bx, hy, hx): # cnt, ry, rx, by, bx
    dq = deque()
    dq.append([0, ry, rx, by, bx])
    result = 0

    while dq:
        cnt, ry, rx, by, bx = dq.popleft()
        if cnt > 10:
            break
        for i in range(4):
            b_check, next_by, next_bx, b_cnt = move(i, by, bx, hy, hx)
            if b_check:
                continue
            r_check, next_ry, next_rx, r_cnt = move(i, ry, rx, hy, hx)
            if r_check:
                result = 1
                break
            if next_ry == next_by and next_rx = next_bx:
                next_ry, next_rx, next_by, next_bx = compare_rb(i, next_ry, next_rx, next_by, next_bx, b_cnt > r_cnt)
            
            dq.append(cnt + 1, next_ry, next_rx, next_by, next_bx, hy, hx)

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

print(solve(0, red_y, red_x, blue_y, blue_x, hole_y, hole_x))
