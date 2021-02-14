N = int(input())
fee = [list(map(int, input().split())) for _ in range(N)]

#바로 직전에 색칠한 색과 같지 않은 색 중 최소 비용을 더해감
for i in range(1, N) :
  for j in range(3) :
    if j == 0 :
      fee[i][j] += min(fee[i-1][j+1], fee[i-1][j+2])
    elif j == 1 :
      fee[i][j] += min(fee[i-1][j-1], fee[i-1][j+1])
    else : #j == 2
      fee[i][j] += min(fee[i-1][j-2], fee[i-1][j-1])

print(min(fee[-1]))