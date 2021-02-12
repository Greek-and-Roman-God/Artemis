N = int(input())

#0을 미리 넣어 IndexError가 나지 않도록 한다
stairs = [0 for _ in range(300)]
dp = [0 for _ in range(300)] #현재 계단까지의 최댓값을 저장

for i in range(N) :
  stairs[i] = int(input())

dp[0] = stairs[0] #첫 번째 계단
dp[1] = stairs[0] + stairs[1] #두 번째 계단
#세 번째 계단은 첫 번째+세 번째와 두 번째+세 번째 중 큰 값
dp[2] = max(stairs[1] + stairs[2], stairs[0] + stairs[2])

#i번째 계단은 i-2번째 계단을 밟고 온 경우와
#i-3, i-1번째 계단을 밟고 온 경우 중 큰 값 (3개 연속은 X이므로)
for i in range(3, N) :
  dp[i] = max(stairs[i] + dp[i-2], stairs[i] + stairs[i-1] + dp[i-3])

print(dp[N-1])