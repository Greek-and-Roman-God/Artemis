n = int(input())
arr = [int(input()) for _ in range(n)]

dp = [0 for _ in range(n+1)]
dp[1] = arr[0]
if n > 1 :
  dp[2] = arr[0] + arr[1]
  for i in range(3, n+1) :
    #i번째 포도주를 먹는 경우 (직전 포도주 먹는 경우 / 안 먹는 경우)
    #i번째 포도주를 안 먹는 경우 중 최대값 저장
    dp[i] = max(dp[i-3]+arr[i-2]+arr[i-1], dp[i-2]+arr[i-1], dp[i-1])

print(max(dp))