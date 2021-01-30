from collections import deque

N, K = map(int, input().split())
visited = [0 for _ in range(100001)]
queue = deque([[N, 0]])

#bfs
while queue :
  num = queue.popleft()
  N, cnt = num[0], num[1]
  if N == K :
    break
  visited[N] = 1 #방문한 곳은 재방문하지 않는다
  #cnt를 중복으로 세지 않기 위해 queue에 함께 append
  if N-1 > -1 and visited[N-1] == 0 :
    queue.append([N-1, cnt+1])
  if N+1 < 100001 and visited[N+1] == 0 :
    queue.append([N+1, cnt+1])
  if N*2 < 100001 and visited[N*2] == 0 :
    queue.append([N*2, cnt+1])

print(cnt)