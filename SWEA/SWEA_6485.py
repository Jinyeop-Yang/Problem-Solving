"""
삼성시의 버스 노선
"""
T = int(input())
for tc in range(T):
    N = int(input())
    lis = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    bs, bus = [], [0] * 5001
    t = []
    for i in range(P):
        bs.append(int(input()))
    for a, b in lis:
        for i in range(a, b+1):
            bus[i] += 1
    for i in bs:
        t.append(bus[i])
    print("#{} {}".format(tc+1, ' '.join(map(str, t))))