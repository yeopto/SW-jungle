import sys

def GCD(a, b):
    if a % b == 0:
        return b
    else:
        return GCD(b, a % b)

a, b = map(int, sys.stdin.readline().split())
print(GCD(a, b))