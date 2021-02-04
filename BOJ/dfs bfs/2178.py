from collections import deque

N, M = map(int, input().split())

maze = [list(input()) for _ in range(N)]
dx = [-1, 1, 0, 0] #좌, 우, 상, 하
dy = [0, 0, 1, -1]
cnt = 1

def move(x, y) :
  global cnt
  queue = deque([(x, y, cnt)])
  maze[x-1][y-1] = '0' #(1, 1)을 방문한 것으로 표기

  while queue :
    now = queue.popleft()
    x, y, cnt = now[0], now[1], now[2]
    if (x, y) == (N, M) : #(N, M)에 도착하면 return
      return cnt
    for i in range(4) : #좌, 우, 상, 하를 방문
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 1 or nx > N or ny < 1 or ny > M :
        continue
      if maze[nx-1][ny-1] == '1' : #갈 수 있는 곳을 탐색
        #방문한 곳은 0으로 바꾼다.
        #queue에서 popleft한 뒤에 방문 표시를 하면 시간초과가 나므로 append할 때 방문 표시를 동시에 해줘야 한다 
        maze[nx-1][ny-1] = '0'
        queue.append((nx, ny, cnt+1))

print(move(1, 1))