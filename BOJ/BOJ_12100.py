"""
2048(Easy)
"""
# import sys
# sys.stdin = open("input.txt")
from itertools import product
from copy import deepcopy
def move(S, n):
    temp = n
    for d in range(len(S)):
        if S[d] == 0:
            for i in range(N):
                for j in range(N):
                    if not Map[i][j]: continue
                    cnt = 1; flag = 0
                    while 1:
                        if j + cnt == N or flag: break
                        if Map[j + cnt][i] == 0:
                            cnt += 1; continue
                        else:
                            flag = 1; break
                    if flag:
                        if Map[j][i] == Map[j + cnt][i]:
                            Map[j][i] *= 2
                            Map[j + cnt][i] = 0
                            temp = Map[j][i] if temp < Map[j][i] else temp
                for j in range(N):
                    if Map[j][i] == 0:
                        for k in range(j + 1, N):
                            if Map[k][i] != 0:
                                Map[j][i], Map[k][i] = Map[k][i], Map[j][i]
                                break
        elif S[d] == 1:
            for i in range(N):
                for j in range(N - 1, -1, -1):
                    cnt = 1
                    flag = 0
                    while 1:
                        if j - cnt == -1 or flag: break
                        if Map[j - cnt][i] == 0:
                            cnt += 1; continue
                        else:
                            flag = 1; break
                    if flag:
                        if Map[j][i] == Map[j - cnt][i]:
                            Map[j][i] *= 2
                            Map[j - cnt][i] = 0
                            temp = Map[j][i] if temp < Map[j][i] else temp
                for j in range(N - 1, -1, -1):
                    if Map[j][i] == 0:
                        for k in range(j - 1, -1, -1):
                            if Map[k][i] != 0:
                                Map[k][i], Map[j][i] = Map[j][i], Map[k][i]
                                break
        elif S[d] == 2:
            for i in range(N):
                for j in range(N):
                    cnt = 1
                    flag = 0
                    while 1:
                        if j + cnt == N or flag: break
                        if Map[i][j + cnt] == 0:
                            cnt += 1; continue
                        else:
                            flag = 1; break
                    if flag:
                        if Map[i][j] == Map[i][j + cnt]:
                            Map[i][j] *= 2
                            Map[i][j + cnt] = 0
                            temp = Map[i][j] if temp < Map[i][j] else temp
                for j in range(N):
                    if Map[i][j] == 0:
                        for k in range(j + 1, N):
                            if Map[i][k] != 0:
                                Map[i][j], Map[i][k] = Map[i][k], Map[i][j]
                                break
        elif S[d] == 3:
            for i in range(N):
                for j in range(N - 1, -1, -1):
                    cnt = 1
                    flag = 0
                    while 1:
                        if j - cnt == -1 or flag: break
                        if Map[i][j - cnt] == 0:
                            cnt += 1; continue
                        else:
                            flag = 1; break
                    if flag:
                        if Map[i][j] == Map[i][j - cnt]:
                            Map[i][j] *= 2
                            Map[i][j - cnt] = 0
                            temp = Map[i][j] if temp < Map[i][j] else temp
                for j in range(N - 1, -1, -1):
                    if Map[i][j] == 0:
                        for k in range(j - 1, -1, -1):
                            if Map[i][k] != 0:
                                Map[i][k], Map[i][j] = Map[i][j], Map[i][k]
                                break

    return temp

N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]
cpMap = deepcopy(Map)
lis = list(product(range(4), repeat=5))
temp = 0
for i in range(N):
    temp = max(temp, *Map[i])
res = temp
for i in range(len(lis)):
    n = move(lis[i], res)
    res = res if res > n else n
    Map = deepcopy(cpMap)
print(res)