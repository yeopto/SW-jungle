import sys
input = sys.stdin.readline

N = input()
arr = [*map(int, input().split())]
arr.sort()

answer = 0
sum = 0
for i in arr:
    sum += i
    answer += sum
print(answer)