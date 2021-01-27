import sys
from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
#인접리스트 생성
for _ in range(M) :
  node1, node2 = map(int, sys.stdin.readline().split())
  graph[node1].append(node2)
  graph[node2].append(node1)
for node in graph :
  node.sort() #정점 번호가 작은 것을 먼저 방문하기 위해 정렬

visited = [False] * (N+1)

def dfs(current) :
  visited[current] = True
  print(current, end=' ')

  for i in graph[current] :
    if not visited[i] :
      dfs(i)

def bfs(current) :
  queue = deque([current])
  visited[current] = True

  while queue :
    current = queue.popleft()
    print(current, end=' ')

    for i in graph[current] :
      if not visited[i] :
        queue.append(i)
        visited[i] = True

dfs(V)
print()
visited = [False] * (N+1) #visited를 초기화
bfs(V)