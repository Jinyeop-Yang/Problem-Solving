"""
주사위 굴리기
"""
direction = [
    [3, 2, 6, 1, 5, 4],
    [4, 2, 1, 6, 5, 3],
    [5, 1, 3, 4, 6, 2],
    [2, 6, 3, 4, 1, 5]
]
d = [[0, 1], [0, -1], [-1, 0], [1, 0]]
N, M, y, x, K = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
move = list(map(int, input().split()))
dice, temp = [0] * 6, [0] * 6

for i in move:
    y += d[i-1][0]
    x += d[i-1][1]
    if 0 > y or y >= N or 0 > x or x >= M:
        y -= d[i - 1][0]
        x -= d[i - 1][1]
        continue

    temp = dice[:]
    for j in range(6):
        dice[j] = temp[direction[i-1][j]-1]
    if not Map[y][x]:
        Map[y][x] = dice[5]
    else:
        dice[5], Map[y][x] = Map[y][x], 0
    print(dice[0])