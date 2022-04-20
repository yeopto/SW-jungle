import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

def bfs():
    q = deque()
    visited = [[-1] * n for _ in range(n)] # 문을 부신 갯수 넣어줄 리스트
    q.append((0, 0))
    visited[0][0] = 0
    while q:
        x, y = q.popleft()
        if x == n - 1 and y == n - 1: # 마지막 끝방에 도달하면 종료
            return visited[x][y] 

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1: # 방문하지 않았으면
                if graph[nx][ny] == 1: # 흰방일때
                    q.appendleft((nx, ny)) # 흰방부터 탐색해주기 위해 흰방을 맨 앞에 넣는다.
                    visited[nx][ny] = visited[x][y]
                else:
                    q.append((nx, ny)) # 검은방이면 부신거를 +1 해준다 
                    visited[nx][ny] = visited[x][y] + 1

print(bfs())