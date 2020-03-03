"""
경사로
"""
import sys
sys.stdin = open("input.txt")

N, L = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
res = 0
for i in range(N): # 가로 탐색
    idx, cnt = 1, 1
    while idx < N:
        if Map[i][idx - 1] == Map[i][idx]:
            cnt += 1; idx += 1; continue
        elif abs(Map[i][idx - 1] - Map[i][idx]) >= 2: break
        else:
            if Map[i][idx - 1] < Map[i][idx]:
                if cnt < L: break
                else:
                    idx += 1; cnt = 1; continue
            else:
                temp = 0
                for j in range(idx, N):
                    if Map[i][idx] == Map[i][j]: temp += 1
                    else: break
                if temp >= L:
                    idx += L; cnt = 0; continue
                else: break
    if idx == N: res += 1
for i in range(N): # 세로 탐색
    idx, cnt = 1, 1
    while idx < N:
        if Map[idx - 1][i] == Map[idx][i]:
            cnt += 1; idx += 1; continue
        elif abs(Map[idx - 1][i] - Map[idx][i]) >= 2: break
        else:
            if Map[idx - 1][i] < Map[idx][i]:
                if cnt < L: break
                else:
                    idx += 1; cnt = 1; continue
            else:
                temp = 0
                for j in range(idx, N):
                    if Map[idx][i] == Map[j][i]: temp += 1
                    else: break
                if temp >= L:
                    idx += L; cnt = 0; continue
                else: break
    if idx == N: res += 1
print(res)