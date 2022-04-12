import sys
import heapq

n = int(sys.stdin.readline())
heap = []
for i in range(n):
    x = int(sys.stdin.readline())
    if x:
        heapq.heappush(heap, (-x, x)) # heapq 모듈을 이용하면 결구 최소 힙이 적용되기에 제일 작은 값은 리스트 앞에온다. 그걸 이용해서 튜플로 (-x, x)를 넣어주면 제일 큰 값이 결국 -붙여서 최소가 됨
    else: 
        if len(heap) >= 1:
            print(heapq.heappop(heap)[1]) # 맨 앞에 있는 튜플을 pop해주고 음수가아닌 튜플의 두번째 원소를 출력해주면 최소 힙으로  최대값을 구할 수 있음.
        else:
            print(0)