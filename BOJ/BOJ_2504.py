S = input()
open = [0, 0]
stack = []
flag = 0
for i in range(len(S)):
    if S[i] == '(':
        open[0] += 1
        stack.append(S[i])
    elif S[i] == '[':
        open[1] += 1
        stack.append(S[i])
    elif S[i] == ')':
        if open[0] == 0:
            flag = 1; break
        if stack[len(stack)-1] == '(':
            stack.pop()
            stack.append(2)
            open[0] -= 1
            if type(stack[len(stack)-2]) is int:
                if len(stack) > 2:
                    temp = stack.pop()
                    temp1 = stack.pop()
                    stack.append(temp + temp1)
        elif stack[len(stack)-1] == '[':
            flag = 1; break
        else:
            temp = stack.pop()
            s = stack.pop()
            if s == '(':
                open[0] -= 1
                stack.append(temp*2)
            else:
                flag = 1; break
            if len(stack) > 2:
                if type(stack[len(stack) - 2]) is int:
                    temp = stack.pop()
                    temp1 = stack.pop()
                    stack.append(temp + temp1)
    elif S[i] == ']':
        if open[1] == 0:
           flag = 1; break
        if stack[len(stack)-1] == '[':
            stack.pop()
            stack.append(3)
            open[1] -= 1

            if type(stack[len(stack) - 2]) is int:
                if len(stack) > 2:
                    temp = stack.pop()
                    temp1 = stack.pop()
                    stack.append(temp + temp1)
        elif stack[len(stack)-1] == '(':
            flag = 1; break
        else:
            temp = stack.pop()
            s = stack.pop()
            if s == '[':
                open[1] -= 1
                stack.append(temp*3)
            else:
                flag = 1; break
            if len(stack) > 2:
                if type(stack[len(stack)-2]) is int:
                    temp = stack.pop()
                    temp1 = stack.pop()
                    stack.append(temp + temp1)

for i in stack:
    if i == '(' or i== '[':
        flag = 1; break
if flag == 1: print(0)
else:
    print(sum(stack))

"""
더 쉬운 코드가 많다. 읽고 한번 확인해보고 내꺼 수정도 가능하면 ㄱㄱㄱㄱㄱ
"""
