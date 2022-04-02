import sys, math

a = sys.stdin.readline().split()

A = int(a[0])
B = int(a[1])
V = int(a[2])

answer = (V - B) / (A - B)
print(math.ceil(answer))