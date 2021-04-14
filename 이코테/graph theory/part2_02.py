def team_chk(parent, x) : #같은 팀 여부 확인
  if parent[x] != x : #루트 노드가 본인이 아니라면 재귀
    parent[x] = team_chk(parent, parent[x])
  return parent[x]

def team_union(parent, a, b) : #팀 합치기
  a = team_chk(parent, a)
  b = team_chk(parent, b)
  if a < b : #a와 b의 루트 노드를 비교해 합치기
    parent[b] = a
  else :
    parent[a] = b

N, M = map(int, input().split())
parent = [0 for _ in range(N+1)] #루트 노드를 저장할 공간

for i in range(1, N+1) : #자기 자신으로 루트 노드를 초기화
  parent[i] = i

for i in range(M) :
  op, a, b = map(int, input().split())
  if op == 0 : #연산이 팀 합치기라면
    team_union(parent, a, b)
  elif op == 1 : #연산이 같은 팀 여부 확인이라면
    if team_chk(parent, a) == team_chk(parent, b) :
      print("YES")
    else :
      print("NO")