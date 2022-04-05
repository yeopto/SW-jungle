import sys

N = int(input())
word_list = []

for _ in range(N):
  word_list.append(sys.stdin.readline().rstrip())

set_list = set(word_list) # 중복제거
word_list = list(set_list)  # 다시 리스트로 변경
word_list.sort() # 인자값 비어있으면 문자열은 알파벳순으로 정렬
word_list.sort(key = len) # 정렬 후 문자열 길이 별로 다시 정렬

for word in word_list:
  print(word)