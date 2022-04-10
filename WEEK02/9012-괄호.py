import sys

T = int(sys.stdin.readline())

for str in range(T):
    a = sys.stdin.readline().rstrip()
    str = list(a)
    sum = 0

    for i in str:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
        
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')