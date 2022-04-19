import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0 , -1]

def bfs(matrix, a, b):
    q = deque()
    q.append((a, b))
    matrix[a][b] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = 0
                q.append((nx, ny))
    return 

for _ in range(t):
    cnt = 0
    M, N, K = map(int, input().split())
    matrix = [[0]* M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        matrix[Y][X] = 1
    
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                bfs(matrix, i, j)
                cnt += 1
    print(cnt)