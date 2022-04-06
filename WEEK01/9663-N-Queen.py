import sys

input = sys.stdin.readline

n = int(input())

col = [0] * n
result = 0

def promising(i): # 절대값은 (1,1)에서 (2,2)로 가려면 x축 1, y축 1 가야한다. 즉, 두개의 x좌표 차이와 y좌표 차이가 같으면 대각선에 위치하는 것 
    for k in range(i): # col[i] == col[k]는 행에 동일한 j값이 있는지 확인하는 것이다. (자기 자신에서 행만)
        if col[i] == col[k] or abs(col[i] - col[k]) == i - k: 
            return False
    return True

def dfs(i):
    if i == n:
        global result
        result += 1
        return

    for j in range(n):
        col[i] = j
        if promising(i):
            dfs(i + 1)

dfs(0)

print(result)