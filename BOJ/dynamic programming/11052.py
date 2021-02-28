N = int(input())
P = list(map(int, input().split()))

dp = [0 for _ in range(N+1)]
dp[1] = P[0] #첫 번째 카드 자기 자신
dp[2] = max(P[0] * 2, P[1]) #첫 번째 카드 2개와 두 번째 카드 자기 자신 중 큰 값

for i in range(3, N+1) :
  tmp = []
  for j in range(1, i-1) :
    tmp.append(dp[j] + dp[i-j]) #1번째 카드와 i-1번째 카드, 2번째 카드와 i-2번째 카드, ...
  tmp.append(P[i-1]) #i번째 카드 자기 자신
  dp[i] = max(tmp) #가장 큰 값을 dp에 저장한다

print(dp[N])