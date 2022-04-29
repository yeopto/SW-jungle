import sys
input = sys.stdin.readline

t = int(input())
d = [1, 1, 1, 2, 2]

for i in range(5, 100):
    d.append(d[i -1] + d[i - 5])

for _ in range(t):
    n = int(input())
    print(d[n - 1])