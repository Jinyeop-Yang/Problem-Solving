"""
크로스워드 만들기
"""
a, b = input().split()
Map = ['.'*len(a) for _ in range(len(b))]
aidx = bdix = 0
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            aidx = i
            bidx = j
            break
    else: continue
    break

for i in range(len(b)):
    for j in range(len(a)):
        if i == bidx:
            print(a[j], end='')
        elif j == aidx:
            print(b[i], end='')
        else:
            print(Map[i][j], end='')
    print()