import sys

T = int(input())

for i in range(T):
  R, S = sys.stdin.readline().split()
  text = ''
  for i in S:
    text += int(R) * i
  print(text)