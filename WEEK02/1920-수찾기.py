import sys

n = int(sys.stdin.readline())
A = sorted(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))

def binary(A, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if target == A[mid]:
        return 1
    elif target < A[mid]:
        return binary(A, target, start, mid - 1)
    else:
        return binary(A, target, mid + 1, end)

for target in targets:
    start = 0
    end = len(A) - 1
    print(binary(A, target, start, end))