"""
스도쿠 검증
"""
T = int(input())

for tc in range(T):
    Map = [list(map(int, input().split())) for _ in range(9)]
    flag = 0

    for i in range(9):
        check = [0]*9
        for j in range(9):
            check[Map[i][j]-1] += 1
            if check[Map[i][j]-1] > 1:
                flag = 1; break
        if flag: break
    if not flag:
        for j in range(9):
            check = [0]*9
            for i in range(9):
                check[Map[i][j]-1] += 1
                if check[Map[i][j]-1] > 1:
                    flag = 1; break
            if flag: break
    if not flag:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                check = [0] * 9
                for a in range(i, i+3):
                    for b in range(j, j+3):
                        check[Map[a][b] - 1] += 1
                        if check[Map[a][b] - 1] > 1:
                            flag = 1;
                            break
                    if flag: break

    if flag:
        print("#{} 0".format(tc+1))
    else:
        print("#{} 1".format(tc+1))