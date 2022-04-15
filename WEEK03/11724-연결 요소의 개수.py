import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for i in range(1, M + 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v, visited):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(i, visited)

cnt = 0
for i in range(1, N + 1):
    if visited[i] == False:
        cnt += 1
        dfs(i, visited)

print(cnt)