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