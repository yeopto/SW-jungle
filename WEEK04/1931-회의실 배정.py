import sys
input = sys.stdin.readline

N = int(input())
time = []

for _ in range(N):
    start, end = map(int, input().split())
    time.append([start, end])

time = sorted(time, key=lambda a: a[0])
time = sorted(time, key=lambda a: a[1])

last = 0
count = 0

for i,j in time:
    if i >= last:
        count +=1
        last = j
print(count)