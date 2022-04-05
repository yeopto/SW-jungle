import sys

num_list = []

n = int(input())
for _ in range(n):
  num = int(sys.stdin.readline())
  num_list.append(num)

num_list.sort()

for i in range(len(num_list)):
  print(num_list[i])