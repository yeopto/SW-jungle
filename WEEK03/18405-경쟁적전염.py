import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
virus = []
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            virus.append((graph[i][j], i, j, 0))

S, X, Y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

virus.sort()
q = deque(virus)

while q:
    virus, x, y, time = q.popleft()
    if time == S:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0:
            graph[nx][ny] = virus
            q.append((virus, nx, ny, time + 1))

print(graph[X -1][Y - 1])