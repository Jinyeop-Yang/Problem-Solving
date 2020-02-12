"""
안경이 없어!
파이썬 제출이 없음..
"""
hole = 'CEFGHIJKLMNSTUVWXYZ'
one_hole = 'ADOPQR'
def change(s):
    for i in s:
        if i in hole:
            s = s.replace(i, '!')
        elif i in one_hole:
            s = s.replace(i, '@')
    return s

T = int(input())

for tc in range(T):
    str1, str2 = input().split()
    if len(str1) != len(str2):
        print("#{} DIFF".format(tc+1)); continue
    str1 = change(str1)
    str2 = change(str2)
    print("#{} {}".format(tc+1, 'SAME' if str1 == str2 else 'DIFF'))
