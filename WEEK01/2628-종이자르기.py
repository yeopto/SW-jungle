import sys

r, c = map(int, sys.stdin.readline().split()) # 가로, 세로 크기 입력

row = [0, r] # 0부터 시작하니까 잘리는 부분까지의 길이도 알기 위함
col = [0, c]

for _ in range(int(sys.stdin.readline())): # 잘라야하는 점선 갯수만큼 반복
  rc, line_num = map(int, sys.stdin.readline().split()) # rc = 가로면 0, 세로면 1
  if rc == 1:
    row.append(line_num) # 세로(1)를 자르면 가로길이가 나누어짐
  else:
    col.append(line_num) # 가로(0)를 자르면 세로길이가 나누어짐

row.sort()
col.sort()

gap_maxr = 0
for i in range(1, len(row)): # 가로에서 가장 큰 차이값
  gap = row[i] - row[i - 1]
  if gap_maxr < gap:
    gap_maxr = gap

gap_maxc = 0
for i in range(1, len(col)): # 세로에서 가장 큰 차이값
  gap = col[i] - col[i - 1]
  if gap_maxc < gap:
    gap_maxc = gap

print(gap_maxc * gap_maxr) # 곱해서 가장 큰 넓이 출력