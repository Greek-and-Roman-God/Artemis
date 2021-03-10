import sys

N = int(input())
length = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

result = 0
min_price = price[0]
for i in range(len(length)) :
  if price[i] < min_price : #더 적은 가격이 있으면
    min_price = price[i]
  result += min_price * length[i]

print(result)

#################
#greedy (시간초과)
N = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))

result = price[0] * length[0]
for i in range(1, len(length)) :
  result += min(price[0:i+1]) * length[i]

print(result)

#################
#dp 사용 (시간초과)
N = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))

dp = [0 for _ in range(N+1)]
dp[2] = price[0] * length[0]
dp[3] = min(dp[2] + price[1] * length[1], price[0] * sum(length[0:2]))
for i in range(4, N+1) :
  dp[i] = min(dp[i-1] + price[i-2] * length[i-2], dp[i-1] + price[i-3] * length[i-2], price[0] * sum(length[0:i-1]))

print(dp[N])