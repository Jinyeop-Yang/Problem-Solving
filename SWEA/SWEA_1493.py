"""
수의 새로운 연산
"""
T = int(input())

def f_pos(n):
    x = y = 1
    plus = 2
    cnt = 1
    while cnt < n:
        cnt += plus
        plus += 1
        x += 1
    temp = cnt - n
    return y + temp, x - temp

def f_value(fy, fx):
    x = y = value = 1
    plus = 2
    while x < fx:
        value += plus
        plus += 1
        x += 1
    plus -= 1
    while y < fy:
        value += plus
        plus += 1
        y += 1
    return value
    
for tc in range(T):
    p, q = map(int, input().split())

    py, px = f_pos(p)
    qy, qx = f_pos(q)
    find_y, find_x = py + qy, px + qx

    print("#{} {}".format(tc+1, f_value(find_y, find_x)))