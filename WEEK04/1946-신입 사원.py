import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    grade = []
    count = 1
    N = int(input())
    for _ in range(N):
        a, b = map(int, input().split())
        grade.append((a, b))
    
    grade.sort()

    Max = grade[0][1]

    for i in range(1, N):
        if Max > grade[i][1]:
            count += 1
            Max = grade[i][1]
    print(count)