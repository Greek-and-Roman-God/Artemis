sudoku = [list(map(int, input().split())) for _ in range(9)]
#스도쿠의 빈 곳을 저장
empty = [(i, j) for i in range(9) for j in range(9) if not sudoku[i][j]]

def pick_num(i, j) :
  nums = [i for i in range(1, 10)] #빈 칸에 들어갈 숫자

  #가로 및 세로에 있는 숫자 제거
  for k in range(9) :
    if sudoku[i][k] in nums :
      nums.remove(sudoku[i][k])
    if sudoku[k][j] in nums :
      nums.remove(sudoku[k][j])

  #네모에 있는 숫자 제거
  i //= 3
  j //= 3
  for m in range(i*3, (i+1)*3) :
    for n in range(j*3, (j+1)*3) :
      if sudoku[m][n] in nums :
        nums.remove(sudoku[m][n])

  return nums

flag = False #스도쿠 완성 여부
def play(cnt) :
  global flag
  if flag : #스도쿠를 완성했다면 끝낸다
    return

  if cnt == len(empty) : #빈 칸의 개수만큼 채웠다면
    flag = True
    for i in sudoku :
      print(*i)
    return
  else :
    (i,j) = empty[cnt] #빈 칸의 행,열을 저장
    nums = pick_num(i,j)
    for num in nums :
      sudoku[i][j] = num
      play(cnt+1)
      sudoku[i][j] = 0 #스도쿠가 완성이 안 될 경우 초기화

play(0)