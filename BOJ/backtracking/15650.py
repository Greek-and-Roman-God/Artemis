N, M = map(int, input().split())

visited = [False] * N
result = []

def DFS(temp, N, M, current) :
  if temp == M :
    print(" ".join(map(str, result)))
    return
  
  #탐색 범위를 탐색을 처음 시작한 노드 이후로 조정
  for i in range(current, len(visited)) :
    if not visited[i] :
      visited[i] = True
      result.append(i+1)
      DFS(temp+1, N, M, i)
      visited[i] = False
      result.pop()

DFS(0, N, M, 0)


#combinations 이용한 풀이법
from itertools import combinations

N, M = map(int, input().split())

nums = [i for i in range(1, N+1)]
result = combinations(nums, M)

for i in result :
  print(' '.join(map(str, i)))