"""
[모의 SW 역량테스트] 숫자 만들기
"""
def calc(plus, minus, product, divide, cnt, number):
    if cnt == N-1:
        global max_n, min_n
        max_n = max(number, max_n)
        min_n = min(number, min_n)
        return
    if plus > 0:
        calc(plus - 1, minus, product, divide, cnt + 1, number + numbers[cnt+1])
    if minus > 0:
        calc(plus, minus - 1, product, divide, cnt + 1, number - numbers[cnt+1])
    if product > 0:
        calc(plus, minus, product - 1, divide, cnt + 1, number * numbers[cnt+1])
    if divide > 0:
        calc(plus, minus, product, divide - 1, cnt + 1, int(number / numbers[cnt+1]))

T = int(input())
for tc in range(T):
    N = int(input())
    plus, minus, product, divide = map(int, input().split())
    numbers = list(map(int, input().split()))
    max_n = -10e10
    min_n = 10e10
    cnt = 0
    calc(plus, minus, product, divide, 0, numbers[0])
    print("#{} {}".format(tc+1, max_n - min_n))