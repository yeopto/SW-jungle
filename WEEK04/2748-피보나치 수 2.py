# 탑다운

import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

d = [0] * 100

def fibo(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

n = int(input())

print(fibo(n))

'''
바텀업

import sys
input = sys.stdin.readline

d = [0] * 100

d[0] = 0
d[1] = 1
n = int(input())

for i in range(2, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])
'''