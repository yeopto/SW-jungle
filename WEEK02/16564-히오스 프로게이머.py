import sys

def count(li, mid):
    t = 0
    for n in li:
        if n >= mid:
            break
        t += mid - n
    return t

n, k = map(int, sys.stdin.readline().split())
li = sorted([int(sys.stdin.readline().rstrip()) for _ in range(n)])
start, end = min(li), max(li) + k
result = 0

while start <= end:
    mid = (start + end) // 2
    if count(li, mid) <= k:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)