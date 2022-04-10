import sys

# 행렬 곱셈
def mul(n, matrix1, matrix2):
    result = [[0]* n for _ in range(n)] # N * N 만큼
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j] # matrix1의 열값이 matrix2에선 행의값
            result[i][j] %= 1000

    return result

def devide(n, b, matrix): # b는 몇번 제곱할지/ 예를들어 5번 곱해야하면 5//2 * 5//2 * 1 하면 되는 거기에 b가 1,2인 경우는 조건으로 써주고 3부터는 쪼개서 생각하면 됨.
    if b == 1:
        return matrix
    elif b == 2:
        return mul(n, matrix, matrix)
    else:
        temp = devide(n, b//2, matrix)
        if b % 2 == 0:
            return mul(n, temp, temp) # 짝수면 분할해서 정복하면 됨.
        else:
            return mul(n, mul(n, temp, temp), matrix) # 홀수면 분할해도 하나 남으니까 남은거 곱해주기

n, b = map(int, sys.stdin.readline().split())
matrix = [[*map(int, sys.stdin.readline().split())] for _ in range(n)]

result = devide(n, b, matrix) # mul에서 연산되어 result들이 2차원 배열로 저장되어 있음

for row in result:
    for num in row:
        print(num % 1000, end=' ')
    print()
