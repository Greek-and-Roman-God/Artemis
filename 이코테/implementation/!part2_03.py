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