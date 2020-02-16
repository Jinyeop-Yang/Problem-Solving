"""
[파이썬 S/W 문제해결 기본] 5일차 - 토너먼트 카드게임
어디가 틀렸을까
"""

T = int(input())
for tc in range(T):
    N = int(input())
    lis = list(map(int, input().split()))
    res = 0
    g1 = []
    g2 = []
    for i, n in enumerate(lis):
        if i < N // 2:
            g1.append((i, n))
        else:
            g2.append((i, n))
    # print(g1,g2)
    while len(g1) != 1:
        for i in range(len(g1)//2):
            if (g1[i][1] + 1) == g1[i+1][1] or (g1[i][1] == 3 and g1[i+1][1] == 1):
                g1.pop(i)
            else:
                g1.pop(i+1)
        # print(g1,g2)
    while len(g2) != 1:
        for i in range(len(g2)//2):
            if (g2[i][1] + 1) == g2[i+1][1] or (g2[i][1] == 3 and g2[i+1][1] == 1):
                g2.pop(i)
            else:
                g2.pop(i+1)
    # print(g1,g2)

    print("#{} {}".format(tc+1, g2[0][0] + 1 if g1[0][1] + 1 == g2[0][1] or (g1[i][1] == 3 and g2[i+1][1] == 1) else g1[0][0] + 1))