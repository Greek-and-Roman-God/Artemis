N, M = map(int, input().split())

result = []

def DFS(temp, N, M) :
  if temp == M :
    print(*result)
    return
  
  for i in range(N) :
    result.append(i+1)
    DFS(temp+1, N, M)
    result.pop()

DFS(0, N, M)