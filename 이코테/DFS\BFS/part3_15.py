import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M) :
  A, B = map(int, input().split())
  graph[A].append(B) #단방향 도로 저장

result = []
visited = [False] * (N+1) #방문여부 체크
dist = 0 #시작 거리
queue = deque([(X, dist)])
visited[X] = True
while queue :
  now, dist = queue.popleft()
  if dist == K : #최단 거리가 K인 도시를 발견하면 저장
    result.append(now)

  for i in graph[now] : #도로를 따라 돌면서 방문하지 않은 도시 탐색
    if not visited[i] :
      visited[i] = True
      queue.append((i, dist+1)) #거리를 1씩 늘려가며 queue에 저장

if result :
  result.sort()
  for i in result :
    print(i)
else :
  print(-1)