import sys

def lottery(depth, current) :
  if depth == 6 : #6개를 뽑으면
    print(*result)
    return
  
  for i in range(current, k) :
    if not visited[i] :
      visited[i] = True
      result.append(S[i])
      lottery(depth+1, i)
      result.pop()
      visited[i] = False

while True :
  temp = list(map(int, sys.stdin.readline().split()))
  k = temp[0]
  S = temp[1:]
  if not k : #0이면 멈춤
    break
  
  visited = [False] * k
  result = []
  lottery(0, 0)
  print()