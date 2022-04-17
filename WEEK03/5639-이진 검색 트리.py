import sys
sys.setrecursionlimit(10**9) # 재귀 제한

input = sys.stdin.readline

tree = [] # 전위순회한 노드들

# 문제에 어디까지 받으라는 기준이 없어서 try/except로 해준다.
while True:
    try:
        tree.append(int(input()))
    except:
        break

def post_order(start, end):
    if start > end:
        return
    
    div = end + 1 # 루트보다 큰 값이 존재하지 않을 때를 대비

    for i in range(start + 1, end + 1): # 루트 다음 원소부터, 마지막 원소 까지
        if tree[start] < tree[i]: # 루트 보다 크면 나눠줘
            div = i # 나누는 기준이 되는 인덱스
            break
    
    # 후위 순회
    post_order(start + 1, div - 1) # 왼쪽 자식
    post_order(div, end) # 오른쪽 자식
    print(tree[start]) # 루트 노드

post_order(0, len(tree) - 1) # tree 인덱스 0부터 마지막 원소 인덱스까지