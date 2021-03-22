#210322
N, M = map(int, input().split())
frame = [list(input()) for _ in range(N)]

ice = [] #구멍이 뚫려 있는 부분 저장
for i in range(N) :
  for j in range(M) :
    if frame[i][j] == "0" :
      ice.append((i, j))

dx = [-1, 1, 0, 0] #좌, 우, 상, 하
dy = [0, 0, 1, -1]

visit = [[0] * M for _ in range(N)] #방문여부 체크
cnt = 0
def frozen(x, y) :
  for i in range(4) : #좌우상하를 돌면서
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx > N-1 or ny < 0 or ny > M-1 : continue #범위가 넘어가면 다음 루프
    if not visit[nx][ny] and frame[nx][ny] == "0" : #방문하지 않았고, 구멍이 뚫려 있다면
      visit[nx][ny] = 1
      frozen(nx, ny)

for i, j in ice : #구멍이 뚫려 있는 모든 부분을 돌면서 체크
  if not visit[i][j] :
    frozen(i, j)
    cnt += 1

print(cnt)


#201111
n, m = map(int, input().split())
#frame = [[]]
frame = []
cnt = 0
cnt_list = []

def count_ice(frame, start, visited) :
  for i in range(len(frame[start])) :
    if visited[start][i] == False :
      visited[start][i] = True
      if frame[start][i] == '0' :
        count_ice(frame, start+1, visited)

for i in range(n) :
  temp = []
 # temp.append([])
  input_data = input()
  for j in range(len(input_data)) :
    temp.append(input_data[j:j+1])
  frame.append(temp)

visited = [[False]*m] * n

count_ice(frame, 0, visited)

print(frame)
print(visited)
print(len(cnt_list))