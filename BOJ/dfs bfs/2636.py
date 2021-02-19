from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

cnt, hour = 0, 0 #가장자리 치즈 개수, 지난 시간
while True :
  queue = deque([(0,0)])
  cheese = [] #가장자리 치즈의 좌표를 저장
  while queue :
    now = queue.popleft()
    x, y = now[0], now[1]
    
    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx > N-1 or ny < 0 or ny > M-1 : continue
      #빈 칸에서 탐색을 시작하면 만나는 치즈는 무조건 가장자리
      if board[nx][ny] == 0 : #빈 칸만 저장 (구멍X)
        queue.append((nx, ny))
      elif board[nx][ny] == 1 : #가장자리 치즈만 저장
        cheese.append((nx, ny))
      board[nx][ny] = -1 #방문여부를 체크
  
  if not cheese : #더이상 저장할 가장자리 치즈가 없으면
    break #치즈가 모두 사라졌으므로 반복문 종료
  
  hour += 1
  cnt = len(cheese)
  for i in range(N) :
    for j in range(M) :
      #처음부터 다시 탐색하기 위해 방문여부 체크를 초기화
      #사라진 가장자리 치즈도 0으로 표시해 빈 칸으로 만들어줌
      if board[i][j] == -1 : board[i][j] = 0

print(hour)
print(cnt)