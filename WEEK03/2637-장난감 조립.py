import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())
needs = [[0] * (N + 1) for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
q = deque()

for i in range(M):
    X, Y, K = map(int, input().split())
    graph[Y].append((X, K))
    indegree[X] += 1

for i in range(N + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()

    for next, next_cost in graph[now]:
        if needs[now].count(0) == N + 1: # 기본 부품이면
            needs[next][now] += next_cost
        else:
            for i in range(N + 1):
                needs[next][i] += needs[now][i] * next_cost # now가 5일때 생각
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)

for x in enumerate(needs[N]):
    if x[1] > 0:
        print(*x)
