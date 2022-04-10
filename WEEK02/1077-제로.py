import sys

n = int(sys.stdin.readline())

stack = []

for i in range(n):
    i = int(sys.stdin.readline())
    if i == 0:
        stack.pop()
    else:        
        stack.append(i)


print(sum(stack))