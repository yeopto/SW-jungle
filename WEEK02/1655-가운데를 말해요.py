import heapq
import sys

n = int(sys.stdin.readline())

# 중간 값을 기준으로 작으면 left, 크면 right
# 중간 값은 결국 left에 있어야함. why? 중간 값이 두개면 작은걸 출력해야함.
left_heap = [] # 최대 힙 max -> max가 중간 값
right_heap = [] # 최소 힙 min 
answer = []

for i in range(n):
    num = int(sys.stdin.readline())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, (-num, num))
    else:
        heapq.heappush(right_heap, (num, num))
    
    if right_heap and left_heap[0][1] > right_heap[0][0]: # right 값보다 left 값이 크면 안되고, 크게 되면 바꿔 주어야함
        min = heapq.heappop(right_heap)[0]
        max = heapq.heappop(left_heap)[1]
        heapq.heappush(left_heap, (-min, min))
        heapq.heappush(right_heap, (max, max))
    
    answer.append(left_heap[0][1])

for j in answer:
    print(j)