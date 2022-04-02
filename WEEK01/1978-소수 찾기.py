import sys 

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

def prime(num):
  if num < 2:
    return False
  elif num == 2:
    return True
  for i in range(2, num):
    if num % i == 0:
      return False
  return True

cnt = 0

for list in num_list:
  if prime(list):
    cnt += 1
print(cnt)