"""
[모의 SW 역량테스트] 벽돌 깨기

product 안쓰고 재귀로 중복순열 짜도 시간 비슷한거같은데 흠..
"""
from collections import deque
from itertools import product
from copy import deepcopy
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def solve(permu, cpMap):
    global res
    for i in permu:
        for j in range(H):
            if cpMap[j][i]:
                q = deque()
                q.append((j, i, cpMap[j][i]))
                while q:
                    y, x, n = q.popleft()
                    cpMap[y][x] = 0
                    for a in range(4):
                        for b in range(1, n):
                            ny = y + dy[a] * b
                            nx = x + dx[a] * b

                            if 0 <= ny < H and 0 <= nx < W:
                                if cpMap[ny][nx] == 1:
                                    cpMap[ny][nx] = 0
                                    continue
                                elif cpMap[ny][nx] >= 2:
                                    q.append((ny, nx, cpMap[ny][nx]))
                                    cpMap[ny][nx] = 0
                for a in range(W):
                    temp = []
                    for b in range(H-1, -1, -1):
                        if cpMap[b][a]:
                            temp.append(cpMap[b][a])
                    while len(temp) != H:
                        temp.append(0)
                    for b in range(H-1, -1, -1):
                        cpMap[b][a] = temp[(H-1) - b]
                break
    temp = 0
    for i in range(H):
        for j in range(W):
            if cpMap[i][j]:
                temp += 1
    res = res if res < temp else temp

T = int(input())
for tc in range(T):
    N, W, H = map(int, input().split())
    Map = [list(map(int, input().split())) for _ in range(H)]
    res = float('inf')
    for i in product(range(W), repeat=N):
        cpMap = deepcopy(Map)
        solve(i, cpMap)
        if not res: break
    print("#{} {}".format(tc + 1, res))



"""
from collections import deque
from copy import deepcopy
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def solve(permu, cpMap):
    global res
    for i in permu:
        for j in range(H):
            if cpMap[j][i]:
                q = deque()
                q.append((j, i, cpMap[j][i]))
                while q:
                    y, x, n = q.popleft()
                    cpMap[y][x] = 0
                    for a in range(4):
                        for b in range(1, n):
                            ny = y + dy[a] * b
                            nx = x + dx[a] * b

                            if 0 <= ny < H and 0 <= nx < W:
                                if cpMap[ny][nx] == 1:
                                    cpMap[ny][nx] = 0
                                    continue
                                elif cpMap[ny][nx] >= 2:
                                    q.append((ny, nx, cpMap[ny][nx]))
                                    cpMap[ny][nx] = 0
                for a in range(W):
                    temp = []
                    for b in range(H-1, -1, -1):
                        if cpMap[b][a]:
                            temp.append(cpMap[b][a])
                    while len(temp) != H:
                        temp.append(0)
                    for b in range(H-1, -1, -1):
                        cpMap[b][a] = temp[(H-1) - b]
                break
    temp = 0
    for i in range(H):
        for j in range(W):
            if cpMap[i][j]:
                temp += 1
    res = res if res < temp else temp

def dfs(cnt):
    global flag
    if cnt == N:
        cpMap = deepcopy(Map)
        solve(lis, cpMap)
        if not res:
            flag = 1
        return

    for i in range(W):
        if not flag:
            lis.append(i)
            dfs(cnt + 1)
            lis.pop()
        if flag: return

T = int(input())
for tc in range(T):
    N, W, H = map(int, input().split())
    Map = [list(map(int, input().split())) for _ in range(H)]
    flag, res = 0, float('inf')
    lis = []
    dfs(0)
    print("#{} {}".format(tc + 1, res))
"""