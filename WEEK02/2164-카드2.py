import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque([])

for num in range(1, n + 1):
    q.append(num)

while len(q) != 1:
    q.popleft()
    a = q.popleft()
    q.append(a)

print(*q)