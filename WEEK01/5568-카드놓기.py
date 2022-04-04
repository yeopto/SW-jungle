import sys
from itertools import permutations

n, k = int(input()), int(input()) # 카드갯수, 뽑을갯수

nums = [] # 카드 넣어줄 리스트

result = set() # 카드로 조합한 수 넣는 리스트, set()이용하면 중복되는건 넣을 수 없음

for i in range(n): # 숫자 받아서 리스트에 넣어주고
  num = input()
  nums.append(num)

for per in permutations(nums, k): # 리스트에서 k만큼 뽑아서 순열해준걸 구분자없이해서 result에 넣어줌
  result.add(''.join(per))

print(len(result)) # 중복되지않는 순열화된 수 갯수를 출력