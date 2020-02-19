"""
성곽
이거도 런타임 ㅈㄴ뜬다. 사실 왜 뜨는지는 모르겠다.
메모리 초과 x 시간 초과 x 인덱스 잘못 접근 x 다아닐텐데..
clear를 해준 List에 다시 값을 넣고 받아오려고 해서 그런건가.. 잘 모르겠다. 진짜
그리고 벽하나 뿌수고 얻는 최대값은 원래 카피를 해서 다돌았는데
시간초과 뜰거같아서 다른사람코드 참고했다. 똑똑하네.
"""
import sys
sys.stdin = open("input.txt")
from collections import deque

def bfs(y, x): # 가장 넓은 방의 크기 구함
    q = deque()
    q.append((y, x))
    room = 1
    while q:
        y, x = q.popleft()
        for a in range(4):
            if not Map[y][x] & bit[a]:
                ny = y + d[a][0]
                nx = x + d[a][1]
                if 0 <= ny < m and 0 <= nx < n and not visit[ny][nx]:
                    visit[ny][nx] = 1
                    room_lis.append((ny, nx))
                    room += 1
                    q.append((ny, nx))
    return room

bit = (1, 2, 4, 8) # 좌상우하
d = [[0, -1], [-1, 0], [0, 1], [1, 0]] # 좌상우하
d1 = [[1, 0], [0, 1]]
n, m = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(m)]
visit = [[0] * n for _ in range(m)]
number = 1
room_cnt = room_area = wall = 0

# 맵 돌면서 방의 개수, 가장 넓은 방의 크기는 바로 구함.
for i in range(m):
    for j in range(n):
        if not visit[i][j]:
            room_lis = []
            visit[i][j] = number
            room_cnt += 1
            room_lis.append((i, j))
            temp = bfs(i, j)
            room_area = room_area if room_area > temp else temp
            for a, b in room_lis:
                Map[a][b] = temp
                visit[a][b] = number
            number += 1

# 벽을 하나 제거해서 얻을 수 있는 방의 최대 크기는 visit에 넘버링을 해서 구역을 정하고
# 맵에 구역의 size를 넣어서 우하만 돌면서 다른 넘버링을 가진 놈을 더하고 비교해서 큰 값을 찾음
for i in range(m):
    for j in range(n):
        for a, b in d1:
            ny = i + a
            nx = j + b
            if 0 <= ny < m and 0 <= nx < n and visit[ny][nx] != visit[i][j]:
                wall = wall if wall > Map[ny][nx] + Map[i][j] else Map[ny][nx] + Map[i][j]
print(room_cnt, room_area, wall, sep='\n')