from collections import deque
import copy

N = int(input())

indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
time = [0] * (N+1)

for i in range(1, N+1) :
  lesson = list(map(int, input().split()))
  time[i] = lesson[0]
  for j in lesson[1:-1] :
    indegree[i] += 1
    graph[j].append(i)

result = copy.deepcopy(time)
queue = deque()

for i in range(1, N+1) :
  if not indegree[i] :
    queue.append(i)

while queue :
  now = queue.popleft()
  for i in graph[now] :
    result[i] = max(result[i], result[now] + time[i])
    indegree[i] -= 1
    if not indegree[i] :
      queue.append(i)

for i in range(1, N+1) :
  print(result[i])