"""
[S/W 문제해결 기본] 5일차 - GNS
"""
T = int(input())

for tc in range(T):
    temp = input()
    string = list(map(str, input().split()))
    e_number = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    number = [0] * 10
    result = ''
    for i in range(10):
        number[i] = string.count(e_number[i])
        result += (e_number[i] + ' ') * number[i]
    print("#{}".format(tc+1))
    print(result.rstrip())