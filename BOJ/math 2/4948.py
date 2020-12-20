while True :
  n = int(input())
  if n == 0 : #입력의 마지막
    break
  
  p_num = [True] * (2*n+1)
  p_num[0] = False #0은 소수가 아님
  p_num[1] = False #1은 소수가 아님
  
  for i in range(len(p_num)) :
    if p_num[i] : #True면 실행
      for j in range(i*2, len(p_num), i) :
        p_num[j] = False #소수가 아님
  
  cnt = 0
  for i in range(n+1, 2*n+1) :
    if p_num[i] : #True(소수)의 개수를 구한다
      cnt += 1

  print(cnt)