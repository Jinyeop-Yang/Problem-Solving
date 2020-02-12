"""
ATM
완전 간단한 문제였는데 어렵게 풀려고 했음..
"""
import sys
sys.stdin = open("input.txt")

N = int(input())
people = list(map(int, input().split()))
waiting = []
people.sort()
waiting.append(people[0])
for i in range(1, N):
    time = 0
    for j in range(i):
        time += people[j]
    waiting.append(time + people[i])
print(sum(waiting))