import sys
sys.stdin = open("input.txt", "r")

def Solve(y, x, v):
    v[y][x] = True

    if y == 99:
        if MAP[y][x] == 2:
            return True
        return False

    
    if x == 0:
        if MAP[y][x + 1] == 1 and v[y][x + 1] == False:
            return Solve(y, x + 1, v)
        else:
            return Solve(y + 1, x, v)
    elif x == 99:
        if MAP[y][x - 1] == 1 and v[y][x - 1] == False:
            return Solve(y, x - 1, v)
        else:
            return Solve(y + 1, x, v)            
    else:
        if MAP[y][x - 1] == 1 and v[y][x - 1] == False:
            return Solve(y, x - 1, v)
        elif MAP[y][x + 1] == 1 and v[y][x + 1] == False:
            return Solve(y, x + 1, v)
        else:
            return Solve(y + 1, x, v)

for _ in range(10):
    tc = int(input())
    MAP = [list(map(int, input().split())) for _ in range(100)]
    
    for i in range(100):
        if MAP[0][i] == 1:
            visit = [[0] * 100 for _ in range(100)]
            if Solve(0, i, visit):
                res = i
                break
    
    print("#{} {}".format(tc, res))