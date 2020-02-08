"""
의석이의 세로로 말해요
"""
T = int(input())

for tc in range(T):
    Map = [[0]* 15 for _ in range(5)]
    string = [input() for _ in range(5)]
    length = 0
    res = ''
    for i in range(5):
        if length < len(string[i]):
            length = len(string[i])
    
    for i in range(5):
        for j in range(len(string[i])):
            Map[i][j] = string[i][j]
    for i in range(length):
        for j in range(5):
            if Map[j][i] != 0:
                res += str(Map[j][i])
    print("#{} {}".format(tc+1, res))