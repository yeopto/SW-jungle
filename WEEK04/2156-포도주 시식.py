import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * (n + 1)
d = [0] * (n + 1)

for i in range(1, n + 1):
    arr[i] = int(input())

if n == 1:
    print(arr[n])
elif n == 2:
    print(arr[1] + arr[2])
else:
    d[1] = arr[1]
    d[2] = arr[1] + arr[2]
    d[3] = max(arr[1] + arr[3], arr[2] + arr[3], d[2])

    for i in range(4, n + 1):
        d[i] = max(d[i - 3] + arr[i - 1] + arr[i], d[i - 2] + arr[i], d[i - 1])
    
    print(d[n])