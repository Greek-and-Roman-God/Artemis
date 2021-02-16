n = int(input())

dp = [0 for _ in range(1001)]

dp[1] = 1
dp[2] = 3
for i in range(3, n+1) :
  dp[i] = dp[i-2] * 2 + dp[i-1]

print(dp[n] % 10007)

#2x1: 1가지
#2x2: 3가지
#2x3: 5가지
#2x4: 11가지
#2x5: 21가지
#... 규칙을 찾아내서 위의 점화식을 세울 수 있다.