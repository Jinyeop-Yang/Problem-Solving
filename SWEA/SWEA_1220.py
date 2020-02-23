"""
[S/W 문제해결 기본] 5일차 - Magnetic
한 방향으로만 가능
"""
for tc in range(10):
    N = int(input())
    Map = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    for i in range(N):
        for j in range(N):
            if Map[i][j] == 1:
                if i == N - 1:
                    Map[i][j] = 0; continue
                else:
                    r = i + 1
                    while r < N:
                        if r == N - 1 and not Map[r][j]:
                            Map[i][j] = 0; break
                        elif Map[r][j] == 1:
                            Map[i][j] = 0; break
                        elif Map[r][j] == 2:
                            Map[i][j], Map[r][j] = 0, 0
                            res += 1; break
                        r += 1
            elif Map[i][j] == 2:
                if i == 0:
                    Map[i][j] = 0; continue
                else:
                    r = i - 1
                    while r >= 0:
                        if r == 0 and not Map[r][j]:
                            Map[i][j] = 0; break
                        elif Map[r][j] == 2:
                            Map[i][j] = 0; break
                        elif Map[r][j] == 1:
                            Map[i][j], Map[r][j] = 0, 0
                            res += 1; break
                        r -= 1
    print("#{} {}".format(tc + 1, res))
"""
for tc in range(10):
    N = int(input())
    Map = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    for i in range(N - 1):
        for j in range(N):
            if Map[i][j] == 1:
                y = i
                while 1:
                    y += 1
                    if y < N:
                        if Map[y][j] == 1:
                            break
                        elif Map[y][j] == 2:
                            res += 1; break
                    else: break
    print("#{} {}".format(tc + 1, res))
"""