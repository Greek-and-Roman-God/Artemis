#문제에 제시된 좌표 (왼쪽 아래가 0,0)
#04 14 24 34 44 54 64
#03 13 23 33 43 53 63
#02 12 22 32 42 52 62
#01 11 21 31 41 51 61
#00 10 20 30 40 50 60

#뒤집은 좌표 (왼쪽 위가 0,0)
#00 01 02 03 04 05 06
#10 11 12 13 14 15 16
#20 21 22 23 24 25 26
#30 31 32 33 34 35 36
#40 41 42 43 44 45 46

from collections import deque

M, N, K = map(int, input().split())

maps = [list(0 for _ in range(N)) for _ in range(M)]
for _ in range(K) :
  left_x, left_y, right_x, right_y = map(int, input().split())
  #일반적인 좌표는 왼쪽 위가 0,0부터 시작하니 이에 맞게 변환
  for i in range(M-right_y, M-left_y) :
    for j in range(left_x, right_x) :
      maps[i][j] = 1 #직사각형을 색칠해준다

dx = [-1, 1, 0, 0] #좌 우 상 하
dy = [0, 0, 1, -1] #좌 우 상 하

def bfs(i, j) :
  queue = deque([[i, j]]) #영역 시작 좌표를 queue에 넣어준다
  maps[i][j] = 1 #다시 방문하지 않기 위해 1로 변경
  cnt = 1
  while queue :
    now = queue.popleft()
    x, y = now[0], now[1]
    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx > M-1 or ny < 0 or ny > N-1 : continue
      if maps[nx][ny] == 0 : #색칠되지 않은 곳만 계속 탐색
        queue.append([nx, ny])
        maps[nx][ny] = 1
        cnt += 1
  
  return cnt

area = 0 #영역의 개수
cnts = [] #영역의 넓이
for i in range(M) :
  for j in range(N) :
    if maps[i][j] == 0 : #영역이 시작되면
      cnts.append(bfs(i, j))
      area += 1

print(area)
cnts.sort()
print(*cnts)