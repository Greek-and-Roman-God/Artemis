#제곱수와 제곱수의 중앙에서 cnt 바뀌는 규칙이 존재한다
#1	1		1
#2	1 1		2
#3	1 1 1		3
#4	1 2 1		3
#5	1 2 1 1		4
#6	1 2 2 1		4
#7	1 2 2 1 1		5
#8	1 2 2 2 1		5
#9	1 2 3 2 1		5
#10	1 2 3 2 1 1	6
import math

T = int(input())
for _ in range(T) :
  x, y = map(int, input().split())
  sqrt_length = math.sqrt(y-x)
  cnt = int(sqrt_length) * 2
  if int(sqrt_length) == sqrt_length :
    cnt -= 1
  elif y-x >= (math.pow(int(sqrt_length),2) + math.pow(int(sqrt_length)+1,2))/2 :
    cnt += 1
  print(cnt)

"""
#시간초과

#k-1 k k+1을 이동할 수 있을 때
#k+1을 이동하고 나서 남은 거리가 k, k-1 ... 1의 합 이상이면 K+1을 이동
#아니라면, k를 이동하고 나서 남은 거리가 k-1, k-2 ... 1의 합 이상이면 K를 이동
#전부 아니라면, k-1을 이동

T = int(input())
for _ in range(T) :
  x, y = map(int, input().split())
  
  k = 1
  x = x + k #첫 이동거리는 무조건 1이다.
  cnt = 1
  while x < y :
    k = k + 1
    if y >= (x + k) + sum([i for i in range(0, k)]) :
      pass
    elif y >= (x + k-1) + sum([i for i in range(1, k-1)]) :
      k = k - 1 #이 때의 k는 원래의 k와 같다
    else :
      k = k - 2 #이 때의 k는 원래의 k-1과 같다
    x = x + k
    cnt += 1
  print(cnt)
"""