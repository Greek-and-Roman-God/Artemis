N = int(input())
dp = [0 for _ in range(N)]

dp[0] = 1
dp[1] = 3
for i in range(2, N) :
  dp[i] = dp[i-2] * 2 + dp[i-1]

print(dp[N-1] % 796796)

#1 1
#2 3
#3 5
#4 11
#5 21