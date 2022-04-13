# pypy3

import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
start, end = 1, max(trees)

while start <= end: # start가 더 크면 종료해야함 즉 end가 더 클때는 계속 반복 if문에서는 start > end가 종료조건이 맞다.
    mid = (start + end) // 2

    log = 0
    for i in trees:
        if i >= mid:
            log += i - mid
    
    if log >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end) # start가 end보다 크면 종료되니까 end가 정상값이다.