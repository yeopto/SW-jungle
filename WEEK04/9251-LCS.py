import sys
input = sys.stdin.readline

S1 = input().strip()
S2 = input().strip()
len1 = len(S1)
len2 = len(S2)
LCS = [[0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if S1[i - 1] == S2[j - 1]: # 두 문자열을 비교할때 같으면
            LCS[i][j] = LCS[i - 1][j - 1] + 1 # 대각선 +1을 한다
        else: # 다른 문자면
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1]) # 위,왼쪽 중 큰걸로 
print(LCS[len1][len2])