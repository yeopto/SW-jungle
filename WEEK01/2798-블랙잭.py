from itertools import combinations
import sys

N, M = map(int, sys.stdin.readline().split()) 

card_list = list(map(int, sys.stdin.readline().split()))
answer = 0

for cards in combinations(card_list, 3):
  temp_sum = sum(cards)
  if answer < temp_sum <= M:
    answer = temp_sum
print(answer)