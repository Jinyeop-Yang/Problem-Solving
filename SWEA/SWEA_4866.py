"""
[파이썬 S/W 문제해결 기본] 4일차 - 괄호검사
"""
T = int(input())
for tc in range(T):
    s = input()
    stack = []
    res = 1
    for i in s:
        if i == "(" or i == "{":
            stack.append(i)
        elif i == "}":
            if not stack or stack.pop() == "(":
                res = 0; break
        elif i == ")":
            if not stack or stack.pop() == "{":
                res = 0; break
    if not stack:
        print("#{} {}".format(tc+1, res))
    else:
        print("#{} {}".format(tc+1, 0))