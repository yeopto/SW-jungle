import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]

sonic = deque()
water = deque()
count = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'S':
            sonic.append((i, j))
            visited[i][j] = True
        elif graph[i][j] == '*':
            water.append((i, j))
            visited[i][j] = True
        elif graph[i][j] == 'X':
            visited[i][j] = True

while sonic:
    for i in range(len(water)):
        w_x, w_y = water.popleft()
        for j in range(4):
            nx = w_x + dx[j]
            ny = w_y + dy[j]
            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] == '.':
                    water.append((nx, ny))
                    graph[nx][ny] = '*'
                    visited[nx][ny] = True
    count += 1

    for _ in range(len(sonic)):
        s_x, s_y = sonic.popleft()
        for i in range(4):
            nx = s_x + dx[i]
            ny = s_y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] == '.' and visited[nx][ny] == False:
                    sonic.append((nx, ny))
                    visited[nx][ny] = True
                elif graph[nx][ny] == 'D':
                    print(count)
                    exit(0)

print('KAKTUS')