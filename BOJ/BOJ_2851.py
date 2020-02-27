"""
슈퍼마리오
"""
lis = []
for i in range(10):
    lis.append(int(input()))
res = temp = 0
for i in range(10):
    temp += lis[i]
    if temp == 100:
        res = 100; break
    if abs(100 - temp) <= abs(100 - res):
        if abs(100 - temp) == abs(100 - res):
            res = res if res > temp else temp
        else:
            res = temp
print(res)