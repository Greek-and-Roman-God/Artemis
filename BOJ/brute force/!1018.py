#틀렸습니다

N, M = map(int, input().split())
board = []
for i in range(N) :
  board.append(input())

result = []
for i in range(N-7) :
  for j in range(M-7) :
    cnt1 = 0
    cnt2 = 0
    
    temp = 0
    for k in range(i, i+8) :
      for l in range(j, j+8) :
        if board[i][j] == 'W' :
          if temp % 2 == 0 :
            if board[k][l] != 'W' :
              cnt1 += 1
          else :
            if board[k][l] != 'B' :
              cnt1 += 1
        else :
          if temp % 2 == 0 :
            if board[k][l] != 'B' :
              cnt2 += 1
          else :
            if board[k][l] != 'W' :
              cnt2 += 1
        if l != j+7 :
          temp += 1
    result.append(min(cnt1, cnt2) if cnt1 != 0 and cnt2 != 0 else max(cnt1, cnt2))

print(min(result))