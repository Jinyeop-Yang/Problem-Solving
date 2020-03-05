"""
집합
"""
import sys
M = int(sys.stdin.readline().strip())
visit = [0] * 21
for i in range(M):
    string = sys.stdin.readline().rstrip()
    if len(string.split(' ')) == 2:
        o, n = string.split(' ')
        n = int(n)
    else:
        o = string
    if o == 'add':
        visit[n] = 1
    elif o == 'remove':
        visit[n] = 0
    elif o == 'check':
        if visit[n]:
            print(1)
        else: print(0)
    elif o == 'toggle':
        if not visit[n]:
            visit[n] = 1
        else:
            visit[n] = 0
    elif o == 'all':
        visit = [1] * 21
    elif o == 'empty':
        visit = [0] * 21