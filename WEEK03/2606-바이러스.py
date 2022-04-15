import sys

input = sys.stdin.readline

n = int(input())
edge = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
cnt = 0

for i in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, v, visited):
    visited[v] = True
    global cnt

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            cnt += 1

dfs(graph, 1, visited)

print(cnt)