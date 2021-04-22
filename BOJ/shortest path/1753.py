import heapq #개선된 다익스트라 알고리즘 사용을 위해
import sys

V, E = map(int, input().split())
K = int(input())
INF = 1e9
graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1) #거리를 무한으로 설정

for _ in range(E) :
  u, v, w = map(int, sys.stdin.readline().split())
  graph[u].append((v, w)) #각 노드와 이어진 노드, 가중치를 저장

queue = []
heapq.heappush(queue, (0, K)) #시작 노드는 거리 0
while queue :
  dist, now = heapq.heappop(queue)
  if dist < distance[now] : #저장된 거리보다 짧은 거리를 발견하면 (아직 처리 안 한 노드)
    distance[now] = dist #짧은 거리 저장
    for i in graph[now] : #노드에 연결된 간선을 탐색하며 각 노드들의 짧은 거리를 저장
      next, cost = i[0], i[1]
      if cost + dist < distance[next] :
        heapq.heappush(queue, (cost + dist, next))

for i in range(1, len(distance)) :
  if distance[i] == INF :
    print("INF")
  else :
    print(distance[i])