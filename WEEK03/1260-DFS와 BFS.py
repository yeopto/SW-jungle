from collections import deque
import sys

input = sys.stdin.readline

N, M, V = map(int, input().split())
visited = [False] * (N + 1)
graph = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1): # 정점의 번호가 작은 것 부터 먼저 방문하라함
    graph[i].sort()

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(V)
visited = [False] * (N + 1)
print()
bfs(V)