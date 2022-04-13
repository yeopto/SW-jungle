import sys

input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

for i in num:    
    if  i == int(i ** 0.5) ** 2: # 제곱수인지 확인, 제곱수면 약수가 홀수다. 정수로 바꿔줘야함 제곱근이 실수일 수 있음.
        print(1, end=' ')
    else:
        print(0, end=' ')