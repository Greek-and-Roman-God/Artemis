N, M = map(int, input().split())
board = []
for i in range(N) :
  board.append(input())

result = []
for i in range(N-7) : #보드에서 8열 자를 공간 확보
  for j in range(M-7) : #8행 자를 공간 확보

    cnt = 0 #바꿀 횟수
    temp = 0 #인덱스 0~56 (이전 줄의 마지막 인덱스와 그 다음 줄의 첫 번째 인덱스가 같다 - 짝수 판별을 위해)

    for k in range(i, i+8) :
      for l in range(j, j+8) :
        #체스판의 첫번째 인덱스가 'W'로 시작한다고 가정
        if temp % 2 == 0 :
          if board[k][l] != 'W' :
            cnt += 1
        else :
          if board[k][l] != 'B' :
            cnt += 1

        if l != j+7 : #마지막 인덱스가 아닌 경우 1 증가
          temp += 1
    
    #체스판이 'B'로 시작할 때의 변경 횟수와 비교
    result.append(min(cnt, 64-cnt))
    
print(min(result))