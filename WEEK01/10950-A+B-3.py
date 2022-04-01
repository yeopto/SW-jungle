import sys

T = int(sys.stdin.readline())
a = [sys.stdin.readline().split() for i in range(T)]

for i in range(T):
  answer = int(a[i][0]) + int(a[i][1])
  print(answer)