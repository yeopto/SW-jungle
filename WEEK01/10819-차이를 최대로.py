from itertools import permutations
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

per = permutations(A)
answer = 0

for i in per:
  sum = 0
  for j in range(len(i) - 1): # 6개면 다섯번만 계산하면 되니까
    sum += abs(i[j] - i[j + 1])
  if sum > answer:
    answer = sum

print(answer)