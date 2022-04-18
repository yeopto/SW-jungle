import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1) # 방문하지 않았으면 -1로 한다.

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) # 최단 거리를 구하기 때문에 양방향 관계가 필요없음. 왔던 곳으로 되돌아가면 최단거리가 될 수 없다.

def bfs(start):
    q = deque([start])
    visited[start] = 0

    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == -1:
                visited[i] = visited[v] + 1
                q.append(i)

bfs(x)

for i in range(1, n + 1):
    if visited[i] == k:
        print(i)
if k not in visited:
    print(-1)