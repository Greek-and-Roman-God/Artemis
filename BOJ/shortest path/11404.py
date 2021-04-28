import sys

n = int(input())
m = int(input())

INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m) :
  a, b, c = map(int, sys.stdin.readline().split())
  graph[a][b] = min(c, graph[a][b]) #두 도시를 연결하는 다른 노선의 비용이 더 적을 경우 갱신

for i in range(1, n+1) :
  for j in range(1, n+1) :
    if i == j : graph[i][j] = 0

for k in range(1, n+1) :
  for i in range(1, n+1) :
    for j in range(1, n+1) :
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1) :
  for j in range(1, n+1) :
    print(graph[i][j] if graph[i][j] < INF else 0, end=' ') #갈 수 없는 경우 0을 출력
  print()