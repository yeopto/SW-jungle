import sys

# 원소의 부모노드 찾기
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기 -> union은 부모노드가 다를때만 쓰는 것
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

input = sys.stdin.readline

v, e = map(int, input().split())
parent = [0] * (v + 1) # 각 노드 부모 값을 위해
edges = [] # 간선에 대한 정보를 넣기 위함
res = 0 # cost 총비용을 구하기 위함

for i in range(1, v + 1): # 각 노드 부모를 자기 자신으로 
    parent[i] = i

for _ in range(e): # 간선만큼 정보 받기
    a, b, cost = map(int, input().split())
    edges.append((cost, a , b)) # 튜플로 cost부터 넣어주면 cost 순으로 소트 됨

edges.sort()

for edge in edges:
    cost, a, b = edge
    
    if find(parent, a) != find(parent, b): # 각 노드의 부모 값이 같으면 사이클이 있다는 것 최소신장트리는 사이클이 없어야하니까 조건을 저렇게
        union(parent, a, b) # 사이클이 없으니까 최소신장트리에 합쳐 줌
        res += cost # 그 간선에 대한 비용을 res에 넣어준다.

print(res)