N = int(input())
tri = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N) :
  for j in range(i+1) :
    if j == 0 : #맨 왼쪽
      tri[i][j] += tri[i-1][j]
    elif j == i : #맨 오른쪽
      tri[i][j] += tri[i-1][j-1]
    else : #가운데 수는 위에 있는 수 둘 중 큰 값을 더해줌
      tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])

print(max(tri[N-1]))