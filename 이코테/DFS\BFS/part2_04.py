from collections import deque

N, M = map(int, input().split())
maze = [input() for _ in range(N)]

dx = [-1, 1, 0, 0] #좌, 우, 상, 하
dy = [0, 0, 1, -1]

visit = [[0] * M for _ in range(N)] #방문여부 체크
queue = deque([(0, 0, 1)]) #시작좌표, 움직인 칸 개수
while queue :
  (x, y, cnt) = queue.pop()
  if x == N-1 and y == M-1 : #미로 끝에 도달하면 멈춤
    print(cnt)
    break
  for i in range(4) : #네 방향을 돌면서
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx > N-1 or ny < 0 or ny > M-1 : continue
    if not visit[nx][ny] and maze[nx][ny] == "1" : #방문하지 않았고 길이 있다면
      queue.append((nx, ny, cnt+1))
      visit[nx][ny] = 1