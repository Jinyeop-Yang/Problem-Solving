"""
가능한 시험 점수
0
0, 0 + 2
0, 0 + 2, 0 + 2 + 3
이런식으로 풀어감 중복제거하면서..
다른 사람 코드 참고했음
"""
T = int(input())
for tc in range(T):
    N = int(input())
    lis = list(map(int, input().split()))
    visit = [0] * 10001
    max_s = sum(lis)
    visit[0] = 1
    cnt = 1
    for i in range(N):
        for j in range(max_s, -1, -1):
            if visit[j]:
                if not visit[j + lis[i]]:
                    cnt += 1
                    visit[j + lis[i]] = 1
    print("#{} {}".format(tc + 1, cnt))