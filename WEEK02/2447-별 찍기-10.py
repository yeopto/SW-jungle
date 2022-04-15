import sys

def draw(n) :
    global map

    if n == 3: # 재귀는 항상 종료조건 마지막일때를 생각하자
        map[0][:3] = map[2][:3] = [1] * 3
        map[1][:3] = [1, 0, 1]
        return
    
    a = n // 3 # 분할정복은 항상 조건대로 줄여주자
    draw(n//3) # 줄인 뒤 재귀를 돌리자

    for i in range(3): # 마지막일때만 생각하자
        for j in range(3):
            if i == 1 and j == 1: # 3x3 일때 좌표 1,1은 비어있다. 이것도 마찬가지 마지막을 생각하자
                continue
            for k in range(a):
                map[a * i + k][a * j:a * (j + 1)] = map[k][:a] # 행은 a * i 는 반복문에서 고정일테고 0, 3, 6 에서 각각 k증가 할때마다 기본틀 [k][:a]랑 같다 해준다

input = sys.stdin.readline

N = int(input())

map = [[0 for _ in range(N)] for _ in range(N)] 

draw(N)

for i in map:
    for j in i:
        if j:
            print('*', end='')
        else:
            print(' ', end='')
    print()

