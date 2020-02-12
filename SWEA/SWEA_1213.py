"""
[S/W 문제해결 기본] 3일차 - String
"""
# import sys
# sys.stdin = open("input.txt", "r")

for _ in range(10):
    tc = int(input())
    str1 = input()
    str2 = input()
    cnt = 0

    for i in range(len(str2) - len(str1) + 1):
        if str1 == str2[i:i + len(str1)]: # 찾는 문자열의 크기만큼만 확인하며 전체 문자를 돈다.
            cnt += 1
    print('#{} {}'.format(tc, cnt))
