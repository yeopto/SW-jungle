prime = [False, False] + [True] * 9999 # 0 ~ 10000까지 0,1 은 소수가 아니라서 디폴트 false 적용

for i in range(2, 101): # 에라토스테네스의 체를 사용, 그리고 약수 대칭 특징을 이용해 제곱근까지 확인하면되는 로직 
  if prime[i]:
    for j in range(i + i, 10001, i): # 주어진 수들을 i의 값은 남겨 놓고 자기의 배수만큼 소수가 아니기에 false로 만듦
      prime[j] = False

T = int(input())
for _ in range(T):
  n = int(input())
  for i in range(n//2, 0, -1): # 수를 반 쪼개서 거꾸로 소수 찾기 (위에서 소수리스트는 만들었기에 인덱스별로 소수를 확인가능)
    if prime[i]: # 소수면
      if prime[n - i]: # 그 차이 값이 또 소수면
        print(i, n - i) # 출력
        break