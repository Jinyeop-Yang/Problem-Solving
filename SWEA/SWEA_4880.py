"""
[파이썬 S/W 문제해결 기본] 5일차 - 토너먼트 카드게임
로직 자체가 틀렸었음.
"""
def GBB(s, e):
    if s == e:
        return s
    m1 = GBB(s, (s+e)//2)
    m2 = GBB((s+e)//2 + 1, e)
    if (lis[m2] == 1 and lis[m1] == 3 or
        lis[m2] == 2 and lis[m1] == 1 or
        lis[m2] == 3 and lis[m1] == 2):
        return m2
    else:
        return m1

T = int(input())
for tc in range(T):
    N = int(input())
    lis = list(map(int, (('0 ' + input())).split()))

    print("#{} {}".format(tc+1, GBB(1, N)))