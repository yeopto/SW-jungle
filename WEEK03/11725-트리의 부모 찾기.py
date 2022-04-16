import sys

sys.setrecursionlimit(10000000)
input = sys.stdin.readline

n = int(input())
visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    for i in graph[v]:
        if visited[i] == False:
            visited[i] = v
            dfs(i)

dfs(1)

for x in range(2, n + 1):
    print(visited[x])