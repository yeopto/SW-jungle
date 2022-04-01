import sys

x, y, w, h = map(int, sys.stdin.readline().split())

minimum = min(x, y, h-y, w-x)

print(minimum)