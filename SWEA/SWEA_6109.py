"""
추억의 2048게임
"""
# import sys
# sys.stdin = open("input.txt")

T = int(input())

for tc in range(T):
    n, S = input().split()
    N = int(n)
    Map = [list(map(int, input().split())) for _ in range(N)]
    if S == 'up':
        for i in range(N):
            for j in range(N):
                cnt = 1; flag = 0
                while 1:
                    if j + cnt == N or flag: break
                    if Map[j+cnt][i] == 0: cnt += 1; continue
                    else: flag = 1; break
                if flag:
                    if Map[j][i] == Map[j+cnt][i]:
                        Map[j][i] *= 2; Map[j+cnt][i] = 0
            for j in range(N):
                if Map[j][i] == 0:
                    for k in range(j+1, N):
                        if Map[k][i] != 0:
                            Map[j][i], Map[k][i] = Map[k][i], Map[j][i]; break
    elif S == 'down':
        for i in range(N):
            for j in range(N-1, -1, -1):
                cnt = 1; flag = 0
                while 1:
                    if j - cnt == -1 or flag: break
                    if Map[j-cnt][i] == 0: cnt += 1; continue
                    else: flag = 1; break
                if flag:
                    if Map[j][i] == Map[j-cnt][i]:
                        Map[j][i] *= 2; Map[j-cnt][i] = 0
            for j in range(N-1, -1, -1):
                if Map[j][i] == 0:
                    for k in range(j-1, -1, -1):
                        if Map[k][i] != 0:
                            Map[k][i], Map[j][i] = Map[j][i], Map[k][i]; break
    elif S == 'left':
        for i in range(N):
            for j in range(N):
                cnt = 1; flag = 0
                while 1:
                    if j + cnt == N or flag: break
                    if Map[i][j+cnt] == 0: cnt += 1; continue
                    else: flag = 1; break
                if flag:
                    if Map[i][j] == Map[i][j+cnt]:
                        Map[i][j] *= 2; Map[i][j+cnt] = 0
            for j in range(N):
                if Map[i][j] == 0:
                    for k in range(j+1, N):
                        if Map[i][k] != 0:
                            Map[i][j], Map[i][k] = Map[i][k], Map[i][j]; break
    elif S == 'right':
        for i in range(N):
            for j in range(N-1, -1, -1):
                cnt = 1; flag = 0
                while 1:
                    if j - cnt == -1 or flag: break
                    if Map[i][j-cnt] == 0: cnt += 1; continue
                    else: flag = 1; break
                if flag:
                    if Map[i][j] == Map[i][j-cnt]:
                        Map[i][j] *= 2; Map[i][j-cnt] = 0
            for j in range(N-1, -1, -1):
                if Map[i][j] == 0:
                    for k in range(j-1, -1, -1):
                        if Map[i][k] != 0:
                            Map[i][k], Map[i][j] = Map[i][j], Map[i][k]; break
    print("#{}".format(tc+1))
    for i in range(N):
        print(*Map[i])