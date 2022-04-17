import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
add, minus, mul, div = map(int, input().split())

max_num = -1e9
min_num = 1e9

def dfs(num, idx, add, minus, mul, div):
    global max_num, min_num
    if idx == n:
        max_num = max(max_num, num)
        min_num = min(min_num, num)
        return

    if add > 0:
        dfs(num + nums[idx], idx + 1, add - 1, minus, mul, div)
    if minus > 0:    
        dfs(num - nums[idx], idx + 1, add, minus - 1, mul, div)
    if mul > 0:    
        dfs(num * nums[idx], idx + 1, add, minus, mul - 1, div)
    if div > 0:    
        dfs(int(num / nums[idx]), idx + 1, add, minus, mul, div - 1)

dfs(nums[0], 1, add, minus, mul, div)
print(max_num)
print(min_num)