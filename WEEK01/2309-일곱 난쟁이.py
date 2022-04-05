import sys
from itertools import combinations # 조합 쓸 수 있음

arr = []
for _ in range(9):
  arr.append(int(sys.stdin.readline().strip())) # 배열에 입력한거 다 집어넣기

combination_list = combinations(arr, 7) # 조합 되어있는 하나의 튜플이 combination_list의 원소가 됨

for comb in combination_list:
  if sum(comb) == 100:
    comb_list = list(map(int, comb))
    comb_list.sort()
    for num in comb_list:
      print(num)
    break # 아무거나 하나 출력하면 되어서 하나 출력 끝나면 반복문 빠져 나옴.