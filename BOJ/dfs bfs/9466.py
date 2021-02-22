import sys
sys.setrecursionlimit(10**8) #재귀 깊이 제한을 늘려준다

def project(i) :
  global cnt
  visit[i] = True #방문표시
  team.append(i) #만들어질 팀에 추가해준다

  if choice[i] == i : #자기 자신을 선택한 경우
    team.pop() #밑에서 걸러지지 않기 위해 팀에서 제외한다
  
  if not visit[choice[i]] : #방문하지 않았다면
    project(choice[i])
  else : #방문했다면
    if team : #만들어진 팀이 있는 경우
      temp = 0
      for j in range(len(team)) :
        if team[j] != choice[i] : #순환 케이스를 찾아준다
          temp += 1
        else :
          cnt += temp #순환 케이스에 속하지 않는 학생의 수를 더해준다
          return
    cnt += len(team) #여기까지 왔다면 만들어지지 못한 팀이므로 팀에 속하지 않은 학생의 수에 더해준다
    return

T = int(input())
for _ in range(T) :
  n = int(input())
  choice = [0] + list(map(int, sys.stdin.readline().split())) #0을 앞에 붙여줘서 인덱스에 쉽게 접근하도록 한다

  cnt = 0 #어느 팀에도 속하지 않는 학생 수
  visit = [False] * (n+1) #방문 여부 체크
  for i in range(1, n+1) :
    team = []
    if not visit[i] :
      project(i)

  print(cnt)