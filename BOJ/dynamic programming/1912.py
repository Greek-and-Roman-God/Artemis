n = int(input())
arr = list(map(int, input().split()))

dp = [0 for _ in range(n)]
dp[0] = arr[0]
for i in range(1, n) :
  #지금까지의 최대값과 arr[i] 자체의 값 중 큰 값을 넣어준다
  dp[i] = max(dp[i-1], 0) + arr[i]

#끝까지 더한다고 큰 수가 나오지 않으므로,
#X번까지 더한 것 중 가장 큰 수를 구해야한다.
print(max(dp))

#10
#10-4, -4
#10-4+3, -4+3, 3
#10-4+3+1, -4+3+1, 3+1, 1