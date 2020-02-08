def dir_check(d, str): # 방향을 돌려준다.
    if str == 'D':
        d = (d + 1) % 4
    elif str == 'L':
        d = (d - 1) % 4
    return d

def move(snake): # 방향따라 한칸씩 이동
    if snake[2] == 0:
        snake[1] += 1
    elif snake[2] == 1:
        snake[0] += 1
    elif snake[2] == 2:
        snake[1] -= 1
    elif snake[2] == 3:
        snake[0] -= 1
    return snake

def solve():
    snake = [1, 1, 0]   # 초기 뱀의 위치, 방향
    route.append([1, 1]) # 뱀이 움직이는 경로
    Map[1][1] = 1
    t_idx = end_time = 0

    while 1:
        s = move(snake) # 뱀의 이동
        if s[0] < 1 or s[1] < 1 or N < s[0] or N < s[1] or Map[s[0]][s[1]] == 1:
            end_time += 1
            break
        if Map[s[0]][s[1]] != 2: # 사과가 없으면
            a, b = route.pop(0) # 꼬리 당기기
            Map[a][b] = 0
        Map[s[0]][s[1]] = 1
        route.append([s[0], s[1]])

        snake = s[:] # 이동한 위치를 다시 snake에 저장

        end_time += 1 # 1초 증가

        if t_idx != len(time):
            if end_time == int(time[t_idx][0]): # 이동 시간에 이동
                snake[2] = dir_check(snake[2], time[t_idx][1])
                t_idx += 1
    return end_time

N = int(input())
Map = [[0]*(N+1) for _ in range(N+1)]
time = []
route = []

K = int(input())
for _ in range(K):
    a, b = map(int, input().split())
    Map[a][b] = 2

L = int(input())
for _ in range(L):
    a, b = list(input().split())
    time.append((a,b))

print(solve())