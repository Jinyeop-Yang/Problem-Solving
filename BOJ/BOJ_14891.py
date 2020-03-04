"""
톱니바퀴
"""
import sys
sys.stdin = open("input.txt")

def rotation(n, d):
    if d == 1: # 시계방향
        temp = gear[n].pop()
        gear[n].insert(0, temp)
    else: # 반시계방향
        temp = gear[n].pop(0)
        gear[n].append(temp)

gear = [list(map(int, input())) for _ in range(4)]
rotate, res = [], 0
K = int(input())
for i in range(K):
    rotate.append(list(map(int, input().split())))
# 2 , 6(-2) 비교
for n, d in rotate:
    state = [(n -1, d)]
    t = d
    # 오른쪽
    for i in range(n-1, 4):
        if i == 3: pass
        else:
            if gear[i][2] != gear[i+1][-2]:
                state.append((i + 1, t * (-1)))
                t *= -1
            else: break
    # 왼쪽
    t = d
    for i in range(n-1, -1, -1):
        if i == 0: pass
        else:
            if gear[i][-2] != gear[i-1][2]:
                state.append((i - 1, t * (-1)))
                t *= -1
            else: break
    for a, b in state:
        rotation(a, b)
for i in range(4):
    if gear[i][0]:
        res += (1 << i)
print(res)