N = int(input())
stairs = [int(input()) for stair in range(N)]

result = stairs[N-1]
stair = N-2
cnt = 1
if N == 1 or N == 2 :
  result = sum(stairs) 
else :
  while True :
    result += max(stairs[stair], stairs[stair-1])
    if stairs[stair] >= stairs[stair-1] :
      if cnt == 2 :
        stair -= 2
        cnt = 1
      else :
        stair -= 1
        cnt += 1
    else :
      stair -=2
      cnt = 1
    if stair <= 0 : 
      if not cnt == 2 :
        result += stairs[stair]
      break

print(result)