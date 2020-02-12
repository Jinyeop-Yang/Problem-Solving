"""
[S/W 문제해결 기본] 10일차 - 비밀번호
"""
for tc in range(10):
    n, s = map(str, input().split())
    N = int(n); s = list(s)
    idx = 0

    while idx != len(s)-1:
        if s[idx] == s[idx+1]:
            s.pop(idx+1)
            s.pop(idx)
            idx -=1
        else: idx += 1
    print("#{} {}".format(tc+1, ''.join(s)))