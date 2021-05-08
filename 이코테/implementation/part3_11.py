from collections import deque

N = int(input())
board = [[0] * N for _ in range(N)]

K = int(input())
for _ in range(K) :
  row, col = map(int, input().split())
  board[row-1][col-1] = 1 #사과 위치 저장

L = int(input())
move = {}
for _ in range(L) :
  X, C = input().split()
  move[int(X)] = C #방향 변환 정보 저장

def change(direct, c) :
  if c == "D" : #오른쪽 회전
    direct = (direct + 1) % 4
  else : #왼쪽 회전
    direct = (direct - 1) % 4
  return direct

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
direct = 1 #시작 방향

result = 1 #시작 시간
y, x = 0, 0 #시작 위치
queue = deque([(y, x)])
board[y][x] = 2 #뱀 현재 위치 저장
while True :
  y, x = y + dy[direct], x + dx[direct] #방향에 맞게 뱀이 나아갈 위치 조정
  if y < 0 or y > N-1 or x < 0 or x > N-1 or board[y][x] == 2 : #벽이나 몸에 부딪히면 종료
    print(result)
    break
  else :
    if board[y][x] != 1 : #사과가 없으면 꼬리 제거
      tmp_y, tmp_x = queue.popleft()
      board[tmp_y][tmp_x] = 0
    board[y][x] = 2
    queue.append((y, x))

  if result in move.keys() : #방향 전환 시간이 되었다면 전환
    direct = change(direct, move[result])
  result += 1