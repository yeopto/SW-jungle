import sys

n = int(sys.stdin.readline())

stack = []

for i in range(n):
    i = int(sys.stdin.readline())
    stack.append(i)

cnt = 1
max = stack[-1]

for i in range(len(stack)-1, -1, -1):
    if max < stack[i]:
        cnt += 1
        max = stack[i]

print(cnt)