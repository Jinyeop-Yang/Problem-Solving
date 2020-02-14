"""
색종이 - 2
"""
d = [(1,0),(0,1),(-1,0),(0,-1)]
N = int(input())
Map = [[0]*101 for _ in range(101)]
res = 0
for _ in range(N):
    y, x = map(int, input().split())
    for i in range(y, y + 10):
        for j in range(x, x + 10):
            if Map[i][j] == 0:
                Map[i][j] = 1
for i in range(100):
    for j in range(100):
        if Map[i][j] == 1:
            cnt = 0
            for a, b in d:
                ny = i + a; nx = j + b
                if 0 <= ny < 101 and 0 <= nx < 101:
                    if Map[ny][nx] == 0:
                        cnt += 1
            res += cnt
print(res)