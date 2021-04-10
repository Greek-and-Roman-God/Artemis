INF = int(1e9) #무한 값 설정

N, M = map(int, input().split())
graph = [[INF] * (N+1) for _ in range(N+1)] #이동 비용을 전부 무한으로 설정
for i in range(1, N+1) :
  for j in range(1, N+1) :
    if i == j : graph[i][j] = 0 #자기 자신으로의 이동 비용은 0
for _ in range(M) :
  a, b = map(int, input().split())
  graph[a][b], graph[b][a] = 1, 1 #도로가 연결되어 있는 경우 이동 비용은 1
X, K = map(int, input().split())

#플로이드 워셜 알고리즘
for k in range(1, N+1) :
  for i in range(1, N+1) :
    for j in range(1, N+1) :
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

if graph[1][K] + graph[K][X] < INF : #이동할 수 있는 경우
  print(graph[1][K] + graph[K][X]) #1번 회사에서 K번 회사까지의 거리 + K번 회사에서 X번 회사까지의 거리를 구한다
else :
  print(-1)