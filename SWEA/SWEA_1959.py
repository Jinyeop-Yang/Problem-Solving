"""
두 개의 숫자열
"""
T = int(input())

for tc in range(T):
    N , M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    max_n = 0
    length = abs(len(a) - len(b))

    for i in range(length + 1):
        temp = 0
        if len(a) > len(b):
            for j in range(len(b)):
                temp += (a[j+i] * b[j])
            if max_n < temp:
                max_n = temp
        elif len(a) < len(b):
            for j in range(len(a)):
                temp += (a[j] * b[j+i])
            if max_n < temp:
                max_n = temp
        else:
            for j in range(len(a)):
                temp += (a[j] * b[j])
            max_n = temp
            break
    print("#{} {}".format(tc+1, max_n))