"""
[파이썬 S/W 문제해결 기본] 5일차 - Forth
"""
T = int(input())
for tc in range(T):
    lis = list(map(str, input().split()))
    stack = []
    res = 0
    for i in range(len(lis)-1):
        #if lis[i] == '.': break
        if lis[i].isdigit():
            stack.append(int(lis[i]))
        else:
            if len(stack) < 2:
                res = 'error'; break
            a , b = stack.pop(-2), stack.pop()
            if lis[i] == '+':
                stack.append(a+b)
            elif lis[i] == '-':
                stack.append(a-b)
            elif lis[i] == '*':
                stack.append(a*b)
            elif lis[i] == '/':
                stack.append(a//b)
    else:
        res = stack.pop()
        if len(stack) != 0:
            res = 'error'
    print("#{} {}".format(tc+1, res))
"""
졸라 열받는다. 
 - 도 a, b 바꿔줘야 했음..
#     T = int(input())
# for tc in range(T):
#     lis = list(map(str, input().split()))
#     stack = []
#     res = i = 0
#     while lis[i] != '.':
#         if lis[i].isdigit():
#             stack.append(int(lis[i]))
#         else:
#             if len(stack) < 2:
#             	res = 'error'; break
#             a, b = stack.pop(), stack.pop()
#             if lis[i] == '+':
#                 stack.append(a + b)
#             elif lis[i] == '-':
#                 stack.append(b - a)
#             elif lis[i] == '/':
#                 stack.append(b // a)
#             elif lis[i] == '*':
#                 stack.append(a * b)
#         i += 1
#     else:
#         res = stack.pop()
#         if len(stack) != 0:
#             res = 'error'
#     print("#{} {}".format(tc+1, res))
"""