import sys
input = sys.stdin.readline

N, K = map(int, input().split())
data = [int(input()) for _ in range(N)]
count = 0
data.sort(reverse=True)

for i in data:    
    count += K // i # 몫 만큼 더하기
    K %= i # 나머지 부여

print(count)

''' 조건문 때문에 시간이 더 걸림
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
data = [int(input()) for _ in range(N)]
count = 0
data.sort(reverse=True)

for i in data:
    if K >= i:
        count += K // i # 몫 만큼 더하기
        K %= i # 나머지 부여
        if K <= 0: # K가 0이되면 반복문 탈출
            break
print(count)
'''