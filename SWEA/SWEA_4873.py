"""
[파이썬 S/W 문제해결 기본] 4일차 - 반복문자 지우기
"""
T = int(input())
for tc in range(T):
    stack = []
    s = input()
    for i in s:
        if not stack:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    print("#{} {}".format(tc+1, len(stack)))