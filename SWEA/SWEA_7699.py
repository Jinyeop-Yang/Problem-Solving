"""
수지의 수지 맞는 여행

일케 풀긴 했는데 python이 없어서 제출은 못함
맞는지는 모르겠다. 백준에 1987 알파벳 과 동일한 문제인 듯!
"""
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

T = int(input())
for tc in range(T):
    R, C = map(int, input().split())
    Map = [list(input()) for _ in range(R)]
    visit = [[0] * C for _ in range(R)]
    res = [[''] * C for _ in range(R)]
    l = 0
    q = deque()
    q.append((0, 0, Map[0][0]))
    res[0][0] += Map[0][0]

    while q:
        y, x, s = q.popleft()
        l = max(len(s), l)

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < R and 0 <= nx < C and Map[ny][nx] not in s:
                if not visit[ny][nx]:
                    visit[ny][nx] = 1
                    res[ny][nx] = Map[ny][nx] + s
                    q.append((ny, nx, res[ny][nx]))
                elif len(res[ny][nx]) <= len(Map[ny][nx] + s):
                    res[ny][nx] = Map[ny][nx] + s
                    q.append((ny, nx, res[ny][nx]))
    print("#{} {}".format(tc + 1, l))