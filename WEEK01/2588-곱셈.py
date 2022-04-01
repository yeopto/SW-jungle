import sys

a = int(sys.stdin.readline())
b = sys.stdin.readline()

answer1 = a * int(b[2])
answer2 = a * int(b[1])
answer3 = a * int(b[0])

print(answer1)
print(answer2)
print(answer3)
print(answer1 + (answer2 * 10) + (answer3 * 100))