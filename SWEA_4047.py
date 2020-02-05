# import sys
# sys.stdin = open("input.txt")

T = int(input())

for tc in range(T):
    card = [[0] * 14 for _ in range(4)] # S D H C
    string = input()
    s, d, h, c, res = 0, 0, 0, 0, 0

    for i in range(0, len(string), 3):
        temp = string[i+1] + string[i+2]
        if string[i] == 'S':
            if card[0][int(temp)] == 0:
                card[0][int(temp)] = 1
                s += 1
            else: res = -1; break
        elif string[i] == 'D':
            if card[1][int(temp)] == 0:
                card[1][int(temp)] = 1
                d += 1
            else: res = -1; break
        elif string[i] == 'H':
            if card[2][int(temp)] == 0:
                card[2][int(temp)] = 1
                h += 1
            else: res = -1; break
        elif string[i] == 'C':
            if card[3][int(temp)] == 0:
                card[3][int(temp)] = 1
                c += 1
            else: res = -1; break

    if res == -1:
        print("#{} ERROR".format(tc+1))
    else:
        print("#{} {} {} {} {}".format(tc+1, 13-s, 13-d, 13-h, 13-c))