import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(' ')))

arr.sort()

left = 0
right = n - 1

answer = 20000000001
final = []

while left < right:
    s_left = arr[left]
    s_right = arr[right]

    total = s_left + s_right

    if abs(total) < answer:
        answer = abs(total)
        final = [s_left, s_right]
    
    if total < 0:
        left += 1
    else:
        right -= 1

print(final[0], final[1])