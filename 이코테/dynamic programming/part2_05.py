N, M = map(int, input().split())
money = [int(input()) for _ in range(N)]

dp = [-1 for _ in range(10001)]
for i in range(N) : #가지고 있는 화폐는 바로 만들 수 있음
  dp[money[i]] = 1

for i in range(1, M+1) :
  for j in range(N) :
    tmp = []
    #dp[i - money[j]]를 만드는 방법이 있다면 dp[i]도 만들 수 있음
    if i - money[j] < 1 : continue #인덱스를 벗어나는 경우
    elif dp[i - money[j]] == -1 : continue #dp[i - money[j]]를 만들 수 없는 경우
    else :
      tmp.append(dp[i - money[j]])
  if tmp : #만들 수 있다면
    dp[i] = min(tmp) + 1

print(dp[M])