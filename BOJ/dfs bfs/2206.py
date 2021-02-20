import sys
from collections import deque

N, M = map(int, input().split())
maps = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def wall() :
  queue = deque([[0, 0, 1]]) #x좌표, y좌표, 벽 부술 기회
  visit = [[[0] * 2 for i in range(M)] for i in range(N)] #방문 및 벽 부순 여부 체크
  visit[0][0][1] = 1 #0, 0 좌표에서 벽 부술 기회 1번 있는 채로 시작
  while queue :
    x, y, chance = queue.popleft()
    if x == N-1 and y == M-1 : #N, M에 도달하면 종료
      return visit[x][y][chance]

    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M :
        if maps[nx][ny] == 1 and chance == 1 : #벽이 있고, 부술 기회가 하나 남았으면
          visit[nx][ny][0] = visit[x][y][1] + 1 #벽 부쉈으므로 기회 0, 이전 위치에서 1 움직임
          queue.append([nx, ny, 0]) #앞으로 벽 부술 기회가 0인 상태로 계속 탐색
        elif maps[nx][ny] == 0 and visit[nx][ny][chance] == 0 : #벽이 없고, 방문 안 했으면
          visit[nx][ny][chance] = visit[x][y][chance] + 1 #기회는 이전 그대로, 움직임만 체크
          queue.append([nx, ny, chance]) #기회 그대로 계속 탐색
    
  return -1 #queue를 다 탐색했는데도 N, M에 도달하지 못한 경우

print(wall())

"""
#시간초과

import sys
from collections import deque
import copy

N, M = map(int, input().split())
maps = [list(sys.stdin.readline().strip()) for _ in range(N)]

ones = []
for i in range(N) :
  for j in range(M) :
    if maps[i][j] == '1' :
      ones.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
cnts = []

for i, j in ones :
  temp = copy.deepcopy(maps)
  temp[i][j] = '0'
  cnt = 1
  queue = deque([(0, 0, cnt)])

  while queue :
    now = queue.popleft()
    x, y, cnt = now[0], now[1], now[2]
    if (x, y) == (N-1, M-1) :
      cnts.append(cnt)
      break

    for k in range(4) :
      nx = x + dx[k]
      ny = y + dy[k]
      if nx < 0 or nx > N-1 or ny < 0 or ny > M-1 :
        continue
      else :
        if temp[nx][ny] == '0' :
          temp[nx][ny] = '1'
          queue.append((nx, ny, cnt+1))

print(min(cnts) if len(cnts) else -1)
"""