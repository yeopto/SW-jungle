# 집과 사무실의 위치 모두 철로 선에 포함되는 최대 사람 수를 구하기

import sys
import heapq

n = int(sys.stdin.readline())
arr = [] # 좌표 값 sort 할 것
heap = [] 
maxi = 0 # 몇명인지 확인 할 변수

for i in range(n):
    h, o = map(int, sys.stdin.readline().split())
    if h > o:
        arr.append([o, h])
    else:
        arr.append([h, o])

d = int(sys.stdin.readline())
arr.sort(key=lambda x: x[1]) # rp 기준으로 오름차순 정렬

for i in range(len(arr)):
    lp = arr[i][0]
    rp = arr[i][1]

    if rp - lp <= d: # 애초에 길이가 d 보다 크면 볼 필요가 없기에 d만큼에 포함되는 것만 lp를 힙에 넣어 줌
        heapq.heappush(heap, lp)
    else:
        continue

    while len(heap) != 0: # 힙에 넣어준값과 rp와 비교하면서
        temp = heap[0] # 기준 값은 제일 작은 0번째 인덱스가 되어야함.
        if rp - temp <= d: # rp 값에서 기준 점을 뺀 것이 d보다 작으면 포함된거니까 중지. 
            break
        else: 
            heapq.heappop(heap)

    maxi = max(maxi, len(heap)) # maxi 값 갱신. rp -temp <= d 조건이 만족하면 maxi는 갱신되겠지만 조건이 만족 안하는 순간부터는 pop 해줘서 maxi가 len보다 클 수 밖에 없음
    # 즉, 갱신이 안됨.
print(maxi)