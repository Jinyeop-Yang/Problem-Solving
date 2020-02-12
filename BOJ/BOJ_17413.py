"""
단어 뒤집기 2
"""
s = input()

i = flag = 0
res = ''
while i <len(s):
    if s[i] == '<':
        while s[i] != '>':
            res += s[i]
            i += 1
        res += '>'
        i += 1
    else:
        temp = ''
        while s[i] != ' ' and s[i] != '<':
            temp += s[i]
            i += 1
            if i == len(s): flag = 1; break
        if flag == 1:
            i -= 1
        if s[i] == ' ':
            res += temp[::-1] + ' '
            i += 1
        else:
            res += temp[::-1]
        if flag==1:
            break
print(res)