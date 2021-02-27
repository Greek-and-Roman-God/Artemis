N = int(input())
A = list(map(int, input().split()))

dp = [0 for _ in range(N)]
dp[0] = 1 #첫 번째 수는 증가하는 부분 수열의 길이가 무조건 1이다

for i in range(1, N) :
  cnt = 0 #증가하는 부분 수열의 길이
  for j in range(i) : #i번째까지의 수 중에서
    if A[j] < A[i] : #i번째 수보다 작은 수 중
      cnt = max(cnt, dp[j]) #제일 긴 증가하는 부분 수열의 길이를 구하고
  dp[i] = cnt + 1 #수열의 길이를 하나 늘려준다

print(max(dp))

#2 54 77 21 14 32 68 47 22 10 6 85 77 85 111 140 25 43 31 11
#1 2  3  2  2  3  4 ...