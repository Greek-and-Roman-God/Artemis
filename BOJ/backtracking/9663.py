N = int(input())

board = [False] * N
diag_l = [False] * (2*N-1)
diag_r = [False] * (2*N-1)

result = 0
def nqueen(i) :
  global result
  if i == N :
    result += 1
    return

  for j in range(N) :
    if not(board[j] or diag_l[i+j] or diag_r[i-j+N-1]) :
      board[j] = diag_l[i+j] = diag_r[i-j+N-1] = True
      nqueen(i+1)
      board[j] = diag_l[i+j] = diag_r[i-j+N-1] = False

nqueen(0)
print(result)