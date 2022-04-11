import sys

N, K = map(int, sys.stdin.readline().split())
nums = list(sys.stdin.readline())
k, stack = K, []

for i in range(N):
    while k > 0 and stack and stack[-1] < nums[i]: # 앞에 숫자가 해당 숫자보다 작을 경우 지워줌
        stack.pop()
        k -= 1
    stack.append(nums[i])
print(''.join(stack[:N - K]))