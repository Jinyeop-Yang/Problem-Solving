"""
4연산
"""
import sys
sys.stdin= open("input.txt")
from collections import deque

s, t = map(int, input().split())
max_n = t + 1
op = ['*','+','-','/']
q = deque()
visit = []
res = ''
if s == t:
    print(0)
else:
    q.append((s, res))
    while q:
        number, op_code = q.popleft()
        if number == t:
            print(op_code)
            break
        for code in op:
            if code == '*':
                if 0 < number * number < max_n and number * number not in visit:
                    q.append((number * number, op_code + code))
                    visit.append(number * number)
            elif code == '+':
                if 0 < number + number < max_n and number + number not in visit:
                    q.append((number + number, op_code + code))
                    visit.append(number + number)
            elif code == '-':
                if 0 <= number - number < max_n and number - number not in visit:
                    q.append((number - number, op_code + code))
                    visit.append(number - number)
            elif code == '/':
                if number != 0 and 0 < number // number < max_n and number // number not in visit:
                    q.append((number // number, op_code + code))
                    visit.append(number // number)
    else:
        print(-1)