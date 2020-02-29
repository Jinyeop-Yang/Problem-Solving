"""
[S/W 문제해결 응용] 7일차 - 금속막대
"""
T = int(input())

for tc in range(T):
    N = int(input())
    temp = list(map(int, input().split()))
    NASA1 = []
    NASA2 = []
    Connect = []
    Connect1 = []

    for i in range(0, N*2, 2):
        NASA1.append([temp[i], temp[i+1]])
        NASA2.extend([temp[i], temp[i+1]])

    for i in range(0, len(NASA2), 2): # 시작점
        if NASA2.count(NASA2[i]) == 1:
            Connect.append([NASA2[i], NASA2[i+1]])
    idx = 0
    while len(Connect) != len(NASA1):
        for i in range(len(NASA2)):
            if i % 2 ==0:
                if Connect[idx][1] == NASA2[i]:
                    Connect.append([NASA2[i], NASA2[i+1]])
        idx += 1

    for i in range(len(Connect)):
        Connect1.append(Connect[i][0])
        Connect1.append(Connect[i][1])

    print("#{} {}".format(tc + 1, ' '.join(map(str, Connect1))))