import sys
input = sys.stdin.readline

N = int(input())
A = [*map(int, input().split())]
B = [*map(int, input().split())]

A.sort()
B.sort(reverse=True)

answer = 0
for i in range(N):
    answer += A[i] * B[i]
print(answer)