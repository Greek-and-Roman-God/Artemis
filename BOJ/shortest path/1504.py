import heapq
import sys

INF = int(1e9)
N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E) :
  a, b, c = map(int, sys.stdin.readline().split())
  graph[a].append((b, c)) #양방향 길이 존재하므로 양 쪽 전부 넣어준다
  graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start) :
  distance = [INF for _ in range(N+1)]
  distance[start] = 0
  queue = []
  heapq.heappush(queue, (0, start))
  while queue :
    dist, now = heapq.heappop(queue)
    for i in graph[now] :
      cost, next = dist + i[1], i[0]
      if cost < distance[next] :
        distance[next] = cost #짧은 거리를 발견하면 갱신
        heapq.heappush(queue, (cost, next))
  return distance

#다익스트라 알고리즘을 각 정점별로 돌려준다
start_node = dijkstra(1)
v1_node = dijkstra(v1)
v2_node = dijkstra(v2)

#두 정점을 거치기만 하면 되므로 어느 정점을 먼저 거치는지는 상관이 없다. 둘 중에 작은 값을 저장한다.
result = min(start_node[v1] + v1_node[v2] + v2_node[N], start_node[v2] + v2_node[v1] + v1_node[N])
print(result if result < INF else -1)


#플로이드 와샬 (시간초과)
import sys

N, E = map(int, input().split())
INF = 1e9
graph = [[INF] * (N+1) for _ in range(N+1)]

for i in range(N+1) :
  for j in range(N+1) :
    if i == j :
      graph[i][j] = 0

for _ in range(E) :
  a, b, c = map(int, sys.stdin.readline().split())
  graph[a][b] = c
  graph[b][a] = c

for i in range(N) :
  for j in range(N) :
    for k in range(N) :
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

v1, v2 = map(int, input().split())

path = min(graph[1][v1] + graph[v1][v2] + graph[v2][N], graph[1][v2] + graph[v2][v1] + graph[v1][N], graph[1][v1] + graph[v1][v2] + graph[v2][1] + graph[1][N], graph[1][v2] + graph[v2][v1] + graph[v1][1] + graph[1][N])
if path < INF :
  print(path)
else :
  print(-1)