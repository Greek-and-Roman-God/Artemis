X = int(input())

dp = [0 for _ in range(X+1)]
for i in range(2, X+1) :
  dp[i] = min(dp[i-1], dp[i//5] if not i % 5 else 30000, dp[i//3] if not i % 3 else 30000, dp[i//2] if not i % 2 else 30000) + 1
  
print(dp[X])