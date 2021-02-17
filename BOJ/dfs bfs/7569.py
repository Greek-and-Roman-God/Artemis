#PyPy3으로 통과

import sys
from collections import deque

M, N, H = map(int, input().split())
box = [[list(sys.stdin.readline().split()) for _ in range(N)] for _ in range(H)] #3차원 배열 생성

queue = deque([])
cnt_one = 0 #익은 토마토
cnt_minus = 0 #토마토가 들어있지 않은 칸
for k in range(H) :
  for i in range(N) :
    for j in range(M) :
      #익은 토마토의 좌표를 day1과 함께 queue에 집어넣어
      #동시에 토마토들이 익을 수 있도록 한다
      if box[k][i][j] == '1' :
        queue.append((k, i, j, 1))
        cnt_one += 1
      elif box[k][i][j] == '-1' :
        cnt_minus += 1

if cnt_one + cnt_minus == M * N * H : #저장할 때 다 익은 경우
  print(0)
else :
  dx = [-1, 1, 0, 0, 0, 0]
  dy = [0, 0, 1, -1, 0, 0]
  dz = [0, 0, 0, 0, 1, -1]
  day = 1
  while queue :
    if cnt_one + cnt_minus == M * N * H : #토마토가 다 익으면
      print(day)
      break
    now = queue.popleft()
    z, x, y, day = now[0], now[1], now[2], now[3]
    for k in range(6) :
      nx = x + dx[k]
      ny = y + dy[k]
      nz = z + dz[k]
      if nx < 0 or nx > N-1 or ny < 0 or ny > M-1 or nz < 0 or nz > H-1 :
        continue
      if box[nz][nx][ny] == '-1' : continue #비어있는 칸은 건너뜀
      elif box[nz][nx][ny] == '0' :
        queue.append([nz, nx, ny, day+1])
        box[nz][nx][ny] = '1'
        cnt_one += 1
  else : #while문에서 break하지 않았다면 모두 익지 않았다는 것
    print(-1)