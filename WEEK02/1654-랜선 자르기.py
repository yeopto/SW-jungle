import sys

input = sys.stdin.readline

K, N = map(int, input().split())
arr = []

for _ in range(K):
    arr.append(int(input()))

arr.sort()

start, end = 1, arr[-1]

while start <= end:
    mid = (start + end)// 2
    lines = 0
    
    for i in arr:
        lines += i // mid

    if lines >= N:
        start = mid + 1
    else:
        end = mid -1

print(end)