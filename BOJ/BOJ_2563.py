"""
색종이
"""
N = int(input())
Map = [[0]*100 for _ in range(100)]
cnt = 0
for _ in range(N):
    y, x = map(int, input().split())
    for i in range(y, y + 10):
        for j in range(x, x + 10):
            if Map[i][j] == 0:
                Map[i][j] = 1; cnt += 1
print(cnt)