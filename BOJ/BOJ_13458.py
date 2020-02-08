"""
시험 감독
"""
N = int(input())
student = list(map(int, input().split()))
B, C = map(int, input().split())
cnt = N

for i in student:
    a = i - B
    if a > 0:
        if (a % C) == 0:
            cnt += a // C
        else:
            cnt += (a//C) + 1
print(cnt)