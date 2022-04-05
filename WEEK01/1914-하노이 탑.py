# 재귀함수는 정의한 대로 코드를 짜야한다.

def hanoi(plate, start, sub, end): # hanoi는 플레이트 갯수만큼 두번째 인자에서 네번째 인자로 플레이트를 옮기는 함수다. 
  if plate == 1:
    print(start, end)
    return
  else :
    hanoi(plate - 1, start, end, sub)
    hanoi(1, start, sub, end)
    hanoi(plate - 1, sub, start, end)

n = int(input())
print(2**n - 1)
if n <= 20:
  hanoi(n, 1, 2, 3)