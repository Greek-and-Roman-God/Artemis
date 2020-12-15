M = int(input())
N = int(input())

min = N
sum = 0
for i in range(M, N+1) :
  if i == 1 : #1은 소수가 아님
    continue
  if i == 2 : #2의 경우는 따로 처리 (반복문에서 걸러지므로)
    min, sum = 2, 2
  else :
    for j in range(2, i) :
      if i % j == 0 :
         break
    else :
      if i < min :
        min = i
      sum  += i

if min == N and sum == 0 :
  print(-1)
else :
  print(sum)
  print(min)