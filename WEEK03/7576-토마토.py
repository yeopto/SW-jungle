import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
#상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

graph = [list(map(int, input().split())) for _ in range(N)]
q = deque()
res = 0
# print(graph)

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append([i,j])

bfs()

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res - 1)