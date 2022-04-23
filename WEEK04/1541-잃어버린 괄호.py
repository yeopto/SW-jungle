'''
최소값을 구하기 위해선 맨처음 '-'를 만나기 전까지는 다 더해주고 
'-'를 만나는 순간 뒤에 있는 숫자들은 다 빼주면 된다.
'''

import sys
input = sys.stdin.readline

num = input().rstrip().split('-')

sum = 0
for i in num[0].split('+'):
    sum += int(i)

for i in num[1:]:
    for j in i.split('+'):
        sum -= int(j)

print(sum)