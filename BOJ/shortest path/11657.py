import sys
INF = int(1e9)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M) :
  A, B, C = map(int, sys.stdin.readline().split())
  graph[A].append((C, B))

def bellman_ford(graph, start) :
  distance = [INF] * (N+1)
  distance[start] = 0

  #N-1번의 갱신
  for _ in range(1, N) :
    for node in range(1, N+1) :
      for cost, neighbor in graph[node] :
        if distance[node] == INF : continue #방문하지 않은 정점은 continue
        if distance[neighbor] > distance[node] + cost :
          distance[neighbor] = distance[node] + cost

  #한 번 더 갱신했을 때 바뀌는 값이 있다면, 사이클이 있다는 것
  for node in range(1, N+1) :
    for cost, neighbor in graph[node] :
      if distance[node] == INF : continue
      if distance[neighbor] > distance[node] + cost :
        print(-1)
        sys.exit()
  
  return distance

result = bellman_ford(graph, 1)
for i in range(2, N+1) :
    print(result[i] if result[i] < INF else -1)