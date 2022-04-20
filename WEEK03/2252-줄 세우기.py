import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1) # 진입 차수

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b) # 방향 그래프라
    indegree[b] += 1 # 진입 차수 증가시켜줘

def topology_sort():
    result = [] # 알고리즘 수행 결과 담을 리스트
    q = deque()
    for i in range(1, N + 1): # 진입 차수 0인 노드 다 삽입
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now) # 하나씩 빼면서 결과리스트에 담기
        
        for i in graph[now]: # 방문한 노드가 생기면 진입 차수 지워주기 위해
            indegree[i] -= 1
            if indegree[i] == 0: #진입 차수가 0이면 다시 삽입
                q.append(i)
    for i in result: # 알고리즘 수행 결과가 위상 정렬된 결과랑 같음
        print(i, end=' ')

topology_sort()