import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for num in range(N):
    num = int(sys.stdin.readline())
    heapq.heappush(heap, num)

if len(heap) == 1: # 한개면 비교를 안해도 됨. 비교횟수 0
    print(0)
else:
    answer = 0
    while len(heap) > 1:
        temp1 = heapq.heappop(heap)
        temp2 = heapq.heappop(heap)
        answer += temp1 + temp2
        heapq.heappush(heap, temp1 + temp2)
    print(answer)