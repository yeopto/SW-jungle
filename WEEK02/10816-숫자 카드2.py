# 1. bisect 풀이

from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline

n = int(input())
arr = sorted(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

def count(arr, left_value, right_value):
    right_index = bisect_right(arr, right_value)
    left_index = bisect_left(arr, left_value)
    return right_index - left_index

for target in targets:
    print(count(arr, target, target), end=' ')

# 2. Counter 풀이

# from collections import Counter
# import sys

# input = sys.stdin.readline

# n = int(input())
# arr = sorted(map(int, input().split()))
# m = int(input())
# targets = list(map(int, input().split()))

# count = Counter(arr)

# for target in targets:
#     if target in count:
#         print(count[target], end=' ')
#     else:
#         print(0, end=' ')