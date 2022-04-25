import sys
input = sys.stdin.readline

N, K = map(int, input().split())
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    w, v = map(int, input().split())
    for j in range(1, K + 1):
        if j < w:
            knapsack[i][j] = knapsack[i - 1][j]
        else:
            knapsack[i][j] = max(knapsack[i - 1][j], knapsack[i - 1][j - w] + v)
    
print(knapsack[N][K])