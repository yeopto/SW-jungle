import sys

N = int(sys.stdin.readline())
top = list(map(int, sys.stdin.readline().split()))
stack = []
answer = []

for i in range(N):
    while stack:
        if stack[-1][1] > top[i]: # 수신 가능 하면
            answer.append(stack[-1][0] + 1) # 스택 top에 저장되어있는 타워인덱스 + 1를 답에 푸시  
            break
        else:
            stack.pop() # 수신 안되면 빼주기
    
    if not stack: # 맨 처음을 위해서
        answer.append(0)
    stack.append([i, top[i]]) # 확인을 위해 스택에 넣어줌 반복할 때 필요없는거면 빼주게 됨.

print(" ".join(map(str, answer)))