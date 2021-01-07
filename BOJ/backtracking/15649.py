N, M = map(int, input().split())

visited = [False] * N #방문여부
result = []

def DFS(temp, N, M) :
  if temp == M :
    print(" ".join(map(str, result)))
    return
  
  for i in range(len(visited)) :  
    if not visited[i] : #방문하지 않은 노드라면
      visited[i] = True
      result.append(i+1)
      DFS(temp+1, N, M) #깊이우선탐색
      visited[i] = False
      result.pop()

DFS(0, N, M)


#permutations 이용한 풀이법
from itertools import permutations

N, M = map(int, input().split())

nums = [i for i in range(1, N+1)]
result = permutations(nums, M)

for i in result :
  for j in range(M) :
    if j+1 != M :
      print(i[j], end=' ')
    else :
      print(i[j])