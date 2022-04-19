import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = []
cnt = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(graph, a, b):
    n = len(graph)
    q = deque()
    q.append((a, b))
    graph[a][b] = 0
    count = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
                count += 1
    return count

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(bfs(graph, i, j))

cnt.sort()
print(len(cnt))

for i in cnt:
    print(i)