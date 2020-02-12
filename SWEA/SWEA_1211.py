"""
[S/W 문제해결 기본] 2일차 - Ladder2
"""
# import sys
# sys.stdin = open("input.txt", "r")
"""
문제 오류가 있음. 도착점이 2가 아니라 1로 되어있다.
SWEA의 INPUT파일에서 2를 찾아볼 수 없음 -> 시간 좀 많이 날림
SWEA_1210과 거의 동일하다.
"""
def Solve(y, x, v, cnt):
    v[y][x] = True

    if y == 99:    # 끝행에 도착하면 이동 횟수를 리턴
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
    idx = 0
    for i in range(100):
        if MAP[0][i] == 1:
            visit = [[0] * 100 for _ in range(100)]
            temp = Solve(0, i, visit, 0)
            if temp <= count:
                if temp == count: # 이동횟수가 같으면 x가 큰 값을 idx에 넣음
                    if idx < i:
                        idx = i
                else:
                    count = temp
                    idx = i

    print("#{} {}".format(tc, idx))