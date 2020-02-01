# import sys
# sys.stdin = open("input.txt", "r")

def Solve(y, x, v):
    v[y][x] = True # 방문했다는 표시

    if y == 99: # 끝 행에 도착했을 때
        if MAP[y][x] == 2: # 도착점이면
            return True
        return False # 도착점이 아닌 끝행이면

    
    if x == 0: # 1열에 있으면 오른쪽만 검사해서 1이 있으면 방향 전환
        if MAP[y][x + 1] == 1 and v[y][x + 1] == False:
            return Solve(y, x + 1, v)
        else: 
            return Solve(y + 1, x, v)
    elif x == 99: # 끝열에 있으면 왼쪽만 검사해서 1이 있으면 방향 전환
        if MAP[y][x - 1] == 1 and v[y][x - 1] == False:
            return Solve(y, x - 1, v)
        else:
            return Solve(y + 1, x, v)            
    else: # 왼쪽과 오른쪽중 갈 수 있는 곳이 있으면 방향전환
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
            if Solve(0, i, visit): # 도착점에 도착이 잘 됐을 경우
                res = i
                break
    
    print("#{} {}".format(tc, res))