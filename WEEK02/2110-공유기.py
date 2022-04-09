n, c = map(int, input().split())

arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()

def binary(arr, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = arr[0]
        count = 1

        for i in range(1, len(arr)):
            if arr[i] >= current + mid:
                count += 1
                current = arr[i]
        
        if count >= c:
            global ans
            start = mid + 1
            ans = mid
        else:
            end = mid - 1

start = 1
end = arr[-1] - arr[0]
ans = 0

binary(arr, start, end)
print(ans)