"""
블랙잭
"""
# import sys
# sys.stdin = open("input.txt")

N, M = map(int, input().split())
card = list(map(int, input().split()))
max_num = -10e6
temp = []
flag = 0
for i in range(N):
    temp.append(card[i])
    for j in range(i+1, N):
        temp.append(card[j])
        for k in range(j+1, N):
            temp.append(card[k])
            if sum(temp) <= M:
                if sum(temp) == M:
                    flag = 1; break
                if sum(temp) > max_num:
                    max_num = sum(temp)
            temp.pop()
            if flag: break
        temp.pop()
        if flag: break
    temp.pop()
    if flag: break
if flag: print(M)
else: print(max_num)