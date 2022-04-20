import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
q = deque()
res = 0

def bfs():
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nz < H and 0 <= nx < N  and 0 <= ny < M and graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                q.append([nz, nx, ny])

for i in range(H):
    for j in range(N): 
        for k in range(M):
            if graph[i][j][k] == 1:
                q.append([i, j, k])

bfs()

for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        res = max(res, max(j))

print(res - 1)