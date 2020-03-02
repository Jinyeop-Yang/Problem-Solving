"""
[모의 SW 역량테스트] 보물상자 비밀번호

print(bin(42), oct(42), hex(42)) --> 각 진수에 맞게 숫자가 출력됨
int('0b101010', 2) -> 2진수를 10진수로 바꿔서 출력됨
int('0o52', 8) -> 8진수를 10진수로 바꿔서 출력됨
int('0x2a', 16) -> 16진수를 10진수로 바꿔서 출력됨

"""
T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    lis = list(input())
    a, t = set(), 0
    while t < N//4:
        for i in range(0, N, N//4):
            a.add(''.join(lis[i : i + N//4]))
        temp = lis.pop(0)
        lis.append(temp)
        t += 1
    numbers = []
    for i in a:
        numbers.append(''.join(map(str, i)))
    numbers.sort(reverse=True)
    res = '0x' + ''.join(numbers[K-1])
    print("#{} {}".format(tc + 1, int(res, 16)))