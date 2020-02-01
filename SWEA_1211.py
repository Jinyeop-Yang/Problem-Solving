import sys
sys.stdin = open("input.txt", "r")

def Solve(y, x, v, cnt):
    v[y][x] = True

    if y == 99:
        return cnt

    if x == 0:
        if MAP[y][x + 1] == 1 and v[y][x + 1] == False:
            return Solve(y, x + 1, v, cnt + 1)
        else:
            return Solve(y + 1, x, v, cnt + 1)
    elif x == 99:
        if MAP[y][x - 1] == 1 and v[y][x - 1] == False:
            return Solve(y, x - 1, v, cnt + 1)
        else:
            return Solve(y + 1, x, v, cnt + 1)            
    else:
        if MAP[y][x - 1] == 1 and v[y][x - 1] == False:
            return Solve(y, x - 1, v, cnt + 1)
        if MAP[y][x + 1] == 1 and v[y][x + 1] == False:
            return Solve(y, x + 1, v, cnt + 1)
        else:
            return Solve(y + 1, x, v, cnt + 1)

for _ in range(10):
    tc = int(input())
    MAP = [list(map(int, input().split())) for _ in range(100)]
    count = 10e10
    idx = 100
    for i in range(100):
        if MAP[0][i] == 1:
            visit = [[0] * 100 for _ in range(100)]
            temp = Solve(0, i, visit, 0)
            if temp <= count:
                if temp == count:
                    if idx > i:
                        idx = i
                else:
                    count = temp
                    idx = i

    print("#{} {}".format(tc, idx))