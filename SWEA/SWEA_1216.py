"""
[S/W 문제해결 기본] 3일차 - 회문2
"""
#import sys
#sys.stdin = open("input.txt", "r")
"""
시간을 줄일 수 있는 방법이 분명 있다. 무엇일까?
"""
for _ in range(10):
    T = int(input())
    MAP = [input() for _ in range(100)]
    length = 0
    # 행에서 회문 찾기
    for i in range(100): # 전체 행
        for j in range(0, 100): # 검사 시작점 한칸씩 이동
            for k in range(j, 100): # 하나씩 늘려나가는
                if MAP[i][j:k + 1] == ''.join(reversed(MAP[i][j: k + 1])):
                    if length < k + 1 - j:
                        length = k + 1 - j
    # 열에서 회문 찾기
    for i in range(100): # 전체 열
        for j in range(0, 100): # 검사 시작점 한칸씩 이동
            string = ''
            for k in range(j, 100): # 하나씩 늘려나가는
                string += MAP[k][i]
                if string == string[::-1]:
                    if length < len(string):
                        length = len(string)

    print('#{} {}'.format(T, length))

"""
다른 사람 코든데 완전 빠름 어케 했는지 분석해보자.

import sys
sys.stdin = open("inputs/palindrome2_input.txt")

def __max_palindrome_len(list_str):

    # SW Expert Academy 1216. 회문 2
    # (https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14Rq5aABUCFAYi&categoryId=AV14Rq5aABUCFAYi&categoryType=CODE)
    
    # 가로 / 세로의 문자열에 존재하는 회문 중에서 최대길이를 찾는 문제
    # :param list_str: 회문 최대길이를 구할 입력값 
    # :return: 문자열 존재하는 회문의 최대길이

    n = len(list_str)
    max_num = 0
    for i in range(n):
        if n - i < max_num:
            break
        l = j = n - 1
        k = i  # l은 현재 끝 길이, i는 시작점 (기준점), k와 j는 회문을 찾기 위한 변수
        while k < j:  # k가 j보다 커지면 회문이라는 뜻이므로 k가 j보다 작은 경우 loop를 돔
            if list_str[k] != list_str[j]:  # 회문이 아니라면 초기화
                l -= 1
                j, k = l, i
            elif list_str[k] == list_str[j]:  # 회문일 가능성이 있다면 안쪽으로 들어가면서 회문 탐색
                k += 1
                j -= 1
                if k >= j:
                    result = l - i + 1  # l - i + 1은 현재 탐색하고있는 회문의 길이
                    max_num = max(max_num, result)
                    break
    return max_num


def solution(input_list):
    n = len(input_list)
    answer = 0
    for i in range(n):
        col_str = []
        for j in range(n):
            col_str.append(input_list[j][i])  # 세로 문자열을 가로로 만듦
        col_max = __max_palindrome_len(col_str)
        row_max = __max_palindrome_len(input_list[i])
        answer = max(answer, row_max, col_max)
    return answer


def main():
    test_cases = 10
    for test_case in range(test_cases):
        input_list = []
        input()
        for _ in range(100):
            input_list.append(input())
        print(f"#{test_case + 1} {solution(input_list)}")


if __name__ == '__main__':
    main()
"""