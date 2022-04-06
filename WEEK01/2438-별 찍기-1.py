# import sys

# N = int(sys.stdin.readline())

# for i in range(1, N + 1):
#   print('*' * i)

def rec(n):
  if n == 0:
    return
  rec(n - 1)
  print('*' * n)

n = int(input())
rec(n)