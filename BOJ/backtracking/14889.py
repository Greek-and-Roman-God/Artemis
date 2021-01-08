N = int(input())

S = []
for _ in range(N) :
  S.append(list(map(int, input().split())))

visited = [False] * N #방문여부 체크
num = N // 2 #절반만 팀 짜면 나머지 팀 완성
result = []

def visit(temp, N, num, start, link, result, current) :
  if temp == num : #팀이 완성되면
    for i in range(N) : #visited의 길이만큼 돌면서
      for j in range(i, N) :
        if visited[i] and visited[j] :
          start += S[i][j] + S[j][i]
        elif not visited[i] and not visited[j] :
          link += S[i][j] + S[j][i]
    result.append(abs(start-link))
    return
  
  #current를 넘겨줘서 중복 탐색을 하지 않아야 시간초과가 안 남
  for i in range(current, N) :
    if not visited[i] :
      visited[i] = True
      visit(temp+1, N, num, start, link, result, i)
      visited[i] = False

visit(0, N, num, 0, 0, result, 0)
print(min(result))