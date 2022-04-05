# 10000개의 배열요소를 만들어서 0으로 만들어주고 입력 받은 값만큼 반복하고 그 인덱스는 1로 만들어준다음
# 값이 1인 인덱스만 찾아서 차례대로 출력해주면 된다.

import sys 

num_list = [0] * 10001 

n = int(sys.stdin.readline())
for _ in range(n):
  num = int(sys.stdin.readline())
  num_list[num] = num_list[num] + 1

for i in range(len(num_list)):
  if num_list[i] != 0:
    for _ in range(num_list[i]):
      print(i)