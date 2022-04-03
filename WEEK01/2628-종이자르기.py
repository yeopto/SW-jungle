import sys

r, c = map(int, sys.stdin.readline().split())

row = [0, r]
col = [0, c]

for _ in range(int(sys.stdin.readline())):
  rc, line_num = map(int, sys.stdin.readline().split())
  if rc == 1:
    row.append(line_num)
  else:
    col.append(line_num)

row.sort()
col.sort()

gap_maxr = 0
for i in range(1, len(row)):
  gap = row[i] - row[i - 1]
  if gap_maxr < gap:
    gap_maxr = gap

gap_maxc = 0
for i in range(1, len(col)):
  gap = col[i] - col[i - 1]
  if gap_maxc < gap:
    gap_maxc = gap

print(gap_maxc * gap_maxr)