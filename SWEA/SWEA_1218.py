"""
[S/W 문제해결 기본] 4일차 - 괄호 짝짓기
"""
for tc in range(10):
    N = int(input())
    s = input()
    res = 1
    check = [0] * 4
    for i in s:
        if i == '(': check[0] += 1
        elif i == ')':
            if not check[0]:
                res = 0; break
            else: check[0] -= 1
        elif i == '[': check[1] += 1
        elif i == ']':
            if not check[1]:
                res = 0; break
            else: check[1] -= 1
        elif i == '{': check[2] += 1
        elif i == '}':
            if not check[2]:
                res = 0; break
            else:
                check[2] -= 1
        elif i == '<': check[3] += 1
        elif i == '>':
            if not check[3]:
                res = 0; break
            else: check[3] -= 1
    print("#{} {}".format(tc + 1, res))