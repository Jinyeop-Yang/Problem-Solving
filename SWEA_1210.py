import sys
sys.stdin = open("input.txt", "r")

def Solve(y, x):
    if MAP[y][x] == 2:
        return True

    if x == 0:
        if MAP[y][x + 1] == 1:
            return Solve(y, x + 1)
        else:
            return Solve(y + 1, x)
    elif x == 99:
        if MAP[y][x - 1] == 1:
            return Solve(y, x - 1)     
    # else:




    return False
for _ in range(10):
    tc = int(input())
    MAP = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if MAP[0][i] == 1:
            if Solve(0, i):
                res = i
                break
    
    print("#{} {}".format(tc, res))