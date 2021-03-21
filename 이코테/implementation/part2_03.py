#210321
N, M = map(int, input().split())
x, y, d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
visit = [list(0 for _ in range(M)) for _ in range(N)]

dx = [-1, 0, 1, 0] #북, 동, 남, 서
dy = [0, 1, 0, -1]

visit[x][y] = 1 #시작부터 방문으로 체크
cnt = 1
while True :
  for i in range(4) :
    nx = x + dx[d % 4]
    ny = y + dy[d % 4]
    if nx < 0 or ny < 0 or nx > N or ny > M : continue
    if not maps[nx][ny] and not visit[nx][ny] : #갈 수 있는 경우
      visit[nx][ny] = 1
      cnt += 1
      x, y = nx, ny
      d += 1
      break
    else : #갈 수 없는 경우 방향만 전환
      d += 1
  else : #네 방향 모두 가봤거나 바다인 경우 뒤로 간다
    nx = x - dx[d % 4]
    ny = y - dx[d % 4]
    if not maps[nx][ny] : #뒤에도 바다인 경우 멈춘다
      break
    else :
      x, y = nx, ny

print(cnt)

#201111
n, m = map(int, input().split())
x, y, direction = map(int, input().split())

map = []
visitied = [[False * m] * n]
for i in range(len(n)) :
  temp = input()
  for j in range(len(temp)) :
    map.append(temp[j:j+1])

#왼쪽, 아래, 오른쪽, 위
position = [[[0],[-1]], [[1],[0]], [[0],[1]], [[-1],[0]]]

def go(x, y, direction) : 
  for i in range(len(position)) :
    visitied[x][y] = True 
    if map[x + position[i][0]][y + position[i][1]] != 1 and not visitied[x + position[i][0]][y + position[i][1]] :
      x = x + position[i][0]
      y = y + position[i][1]

go(x, y, direction)

#True의 개수 세기
cnt = 0
for i in range(len(visitied)) :
  for j in range(len(visitied[i])) :
    if visitied[i][j] :
      cnt += 1
print(cnt)