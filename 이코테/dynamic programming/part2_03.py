N = int(input())
container = list(map(int, input().split()))

dp = [0 for _ in range(N)]
dp[0] = container[0]
dp[1] = max(container[0], container[1])
for i in range(2, N) :
  dp[i] = max(dp[i-2] + container[i], dp[i-1])

print(dp[N-1])