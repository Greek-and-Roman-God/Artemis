n, k = map(int, input().split())

coins = []
for _ in range(n) :
  coins.append(int(input()))

dp = [0 for _ in range(k+1)]
dp[0] = 1
for i in coins :
  for j in range(i, k+1) :
    if j - i >= 0 :
      #i원을 하나 이상 포함해서 j원을 만드는 법은
      #j-i원을 만든 후 i원을 하나 추가하는 것이다
      dp[j] += dp[j-i]

print(dp[k])