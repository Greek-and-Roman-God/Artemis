import heapq
import sys

INF = int(1e9)
T = int(input())
for _ in range(T) :
  n, m, t = map(int, input().split()) #간선, 노드, 목적지 후보 개수
  s, g, h = map(int, input().split()) #출발지, 거쳐가는 노드1, 거쳐가는 노드2

  graph = [[] for _ in range(n+1)]
  for _ in range(m) :
    a, b, d = map(int, sys.stdin.readline().split()) #노드1, 노드2, 간선 길이
    #양방향 도로이므로 양 쪽에 저장
    graph[a].append((b, d))
    graph[b].append((a, d))
  
  destination = [] #목적지 후보 노드들을 저장
  for _ in range(t) :
    destination.append(int(sys.stdin.readline()))
  
  #개선된 다익스트라 알고리즘 사용
  def dijkstra(start) :
    distance = [INF] * (n+1)
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue :
      dist, now = heapq.heappop(queue)
      if distance[now] < dist : continue #저장되어 있는 경로가 더 짧으면 continue
      for i in graph[now] :
        cost, next = dist + i[1], i[0]
        if cost < distance[next] :
          distance[next] = cost
          heapq.heappush(queue, (cost, next))
    
    return distance

  #각 노드별로 다익스트라 알고리즘을 돌린다
  start_node = dijkstra(s)
  g_node = dijkstra(g)
  h_node = dijkstra(h)

  result = [] #가능한 목적지 후보들을 저장
  for i in destination : #특정 노드를 거쳐가는 최단 경로와 목적지까지의 최단 경로가 같다면 저장
    if start_node[g] + g_node[h] + h_node[i] == start_node[i] or start_node[h] + h_node[g] + g_node[i] == start_node[i] :
      result.append(i)

  result.sort()
  for i in result :
    print(i, end=' ')
  print()