"""
정곤이의 단조 증가하는 수
"""
T = int(input())

for tc in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    max_n = -1

    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            temp = str(numbers[i] * numbers[j])
            check = 0
            for k in range(len(temp) - 1):
                if temp[k] > temp[k+1]:
                    check = - 1; break
            if check == - 1: continue
            if max_n < numbers[i] * numbers[j]:
                max_n = numbers[i] * numbers[j]
                
    print("#{} {}".format(tc+1, max_n))