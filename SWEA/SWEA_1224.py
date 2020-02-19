"""
1224. [S/W 문제해결 기본] 6일차 - 계산기3
/ 랑 - 도 넣어야 되는데 안넣음
"""
for tc in range(10):
    N = int(input())
    string = input()
    temp = [] # 연산자
    stack = [] # 후위 표기법
    for i in string:
        if i.isdigit():
            stack.append(i)
        elif i == '(':
            temp.append(i)
        elif i == '*':
            while temp and temp[-1] == '*':
                stack.append(temp.pop())
            temp.append(i)
        elif i == '+':
            while temp and (temp[-1] == '*' or temp[-1] == '+'):
                stack.append(temp.pop())
            temp.append(i)
        elif i == ')':
            while temp[-1] != '(':
                stack.append(temp.pop())
            temp.pop()
            
    while temp:
        stack.append(temp.pop())
    for i in stack:
        if i.isdigit():
            temp.append(int(i))
        elif i == '*':
            temp.append(temp.pop() * temp.pop())
        elif i == '+':
            temp.append(temp.pop() + temp.pop())
            
    print("#{} {}".format(tc + 1, temp[0]))