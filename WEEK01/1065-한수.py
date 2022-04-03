import sys, math

n = int(sys.stdin.readline())

def solution(n):
  count = 0

  for i in range(1, n + 1):
    hundNum = math.floor((i % 1000) / 100)
    tenNum = math.floor((i % 100) / 10)
    oneNum = math.floor(i % 10)

    if i < 100:
      count += 1
    elif i >= 100 and i < 1000:
      if (hundNum - tenNum) == (tenNum - oneNum):
        count += 1
  
  return count

print(solution(n))