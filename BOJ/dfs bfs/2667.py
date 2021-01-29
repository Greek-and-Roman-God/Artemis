import sys

N = int(input())

house_map = []
for _ in range(N) :
  house_map.append(list(sys.stdin.readline()))

apart_complex = []
cnt = 0

#좌, 상, 우, 하
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def complex_num(x, y) :
  global cnt
  house_map[x][y] = '0' #방문한 집은 0으로 변경하여 재방문X
  cnt += 1

  for i in range(4) :
    nx = x + dx[i] #좌, 상, 우, 하를 탐색
    ny = y + dy[i]
    #탐색할 수 없는 지역은 건너뜀
    if nx < 0 or nx >= N or ny < 0 or ny >= N :
      continue
    if house_map[nx][ny] == '1' :
     complex_num(nx, ny)

for i in range(N) :
  for j in range(N) :
    if house_map[i][j] == '1' :
      cnt = 0 #한 단지내 집의 개수를 초기화
      complex_num(i, j)
      apart_complex.append(cnt)

print(len(apart_complex))
apart_complex.sort()
for complex in apart_complex :
  print(complex)