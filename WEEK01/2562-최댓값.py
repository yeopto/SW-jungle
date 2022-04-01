import sys

numbers = []
for i in range(9):
  numbers.append(int(sys.stdin.readline()))

max = numbers[0]
max_idx = 0

for number in numbers:
  if (number > max):
    max = number
    max_idx = numbers.index(number)

print(max)
print(max_idx + 1)