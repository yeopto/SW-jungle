import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

k = int(input())

def dfs(start, group):
    visited[start] = group
    
    for i in graph[start]:
        if visited[i] == False:
            a = dfs(i, -group)
            if a == False:
                return False
        elif visited[i] == visited[start]:
            return False
    return True

for i in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [False] * (v + 1)
    
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v + 1):
        if visited[i] == False:
            result = dfs(i, 1)
            if result == False:
                break
        
    print("YES" if result else "NO")