"""
이모티콘
"""
import sys
sys.stdin = open("input.txt")
from collections import deque

s = int(input())
screen = '1'
clip = ''
visit = set((1, 0))
q = deque()
q.append((screen, clip, 0))
while q:
    sc, cl, t = q.popleft()
    if len(sc) == s:
        print(t); break
    if (sc, cl) not in visit:
        visit.add((sc, cl))
        temp = sc
        temp1 = cl
        # 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
        if cl:
            temp += cl
            q.append((temp, cl, t + 1))
        # 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
        temp1 = sc
        q.append((sc, temp1, t + 1))
        # 화면에 있는 이모티콘 중 하나를 삭제한다.
        sc = sc[:-1]
        q.append((sc, cl, t + 1))
"""
변수 안만들고도 가능
"""
# s = int(input())
# screen = '1'
# clip = ''
# visit = set((screen, clip))
# q = deque()
# q.append((screen, clip, 0))
# while q:
#     sc, cl, t = q.popleft()
#     if len(sc) == s:
#         print(t); break
#     if (sc+cl, cl) not in visit:
#         if cl:
#             q.append((sc+cl, cl, t + 1))
#             visit.add((sc+cl, cl))
#     if (sc, sc) not in visit:
#         q.append((sc, sc, t + 1))
#         visit.add((sc, sc))
#     if (sc[:-1], cl) not in visit:
#         q.append((sc[:-1], cl, t + 1))
#         visit.add((sc[:-1], cl))