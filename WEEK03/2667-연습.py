import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
nums = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    q = deque()
    q.append((a, b))
    graph[a][b] = 0
    count = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or N <= nx or 0 > ny or N <= ny:
                continue
            if graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = 0
                count += 1
    return count

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            nums.append(bfs(i, j))

nums.sort()
print(len(nums))
for num in nums:
    print(num)