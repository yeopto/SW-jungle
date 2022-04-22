import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

max = 100000
visited = [0] * (max + 1)

def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(visited[x])
            break
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= max and visited[nx] == 0:
                visited[nx] = visited[x] + 1
                q.append(nx)

bfs()