import sys
from collections import deque

input = sys.stdin.readline
n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    visited[start] = True
    print(start, end=' ')

    for i in graph[start]:
        if visited[i] == False:
            dfs(i)

def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for i in graph[node]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

dfs(v)
visited = [False] * (n + 1)
print()
bfs(v)