import sys
from collections import deque

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

arr = [[0]* N for _ in range(N)]
for _ in range(K):
    a, b = map(int, sys.stdin.readline().split())
    arr[a - 1][b - 1] = 1 # 사과 저장

def change(d, c):
    # 상(0) 우(1) 하(2) 좌(3)
    # 동쪽 회전: +1
    # 서쪽 회전: -1
    if c == 'L':
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d

# (0,0)기준으로 상 우 하 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def start():
    direction = 1 # 초기 방향 오른쪽으로 가니까 우(1)
    time = 1 # 시간
    y, x = 0, 0 # 초기 뱀 위치
    visited = deque([[y, x]]) # 방문 위치
    arr[y][x] = 2 # 뱀이 지나간 곳은 2로 0,0에서 시작이니까 2로 초기화해준다.
    
    while True:
        y, x = y + dy[direction], x + dx[direction]
        if 0 <= y < N and 0 <= x < N and arr[y][x] != 2: # 벽에 부딪히지 않고 지나가지 않았으면
            if not arr[y][x] == 1: # 사과가 없을 때
                temp_y, temp_x = visited.popleft() # arr[0][0]에서 arr[0][1]로 뱀 머리가 가면 방문도 안했고 사과가 없으니까 visited에서 pop해줘
                arr[temp_y][temp_x] = 0 # 전에 있었던 곳 0으로 만들어주면서 꼬리를 자른다.
            arr[y][x] = 2
            visited.append([y, x])
            if time in times.keys():
                direction = change(direction, times[time])
            time += 1
        else: # 본인 몸에 부딪히거나, 벽에 부딪혔을때
            return time

L = int(sys.stdin.readline())
times = {}
for i in range(L):
    X, C = sys.stdin.readline().split()
    times[int(X)] = C

print(start())