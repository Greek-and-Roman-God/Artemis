N, M = map(int, input().split())

result = []

def DFS(temp, N, M, current) :
  if temp == M :
    print(*result)
    return
  
  for i in range(current, N) :
    result.append(i+1)
    DFS(temp+1, N, M, i)
    result.pop()

DFS(0, N, M, 0)