#시간초과
N = int(input())

S = []
for _ in range(N) :
  S.append(list(map(int, input().split())))

visited = [False] * N
num = N // 2
result = []

def visit(temp, N, num, start, link, result) :
  if temp == num :
    for i in range(N) :
      for j in range(i, N) :
        if visited[i] and visited[j] :
          start += S[i][j] + S[j][i]
        elif not visited[i] and not visited[j] :
          link += S[i][j] + S[j][i]
    result.append(abs(start-link))
    return
  
  for i in range(N) :
    if not visited[i] :
      visited[i] = True
      visit(temp+1, N, num, start, link, result)
      visited[i] = False

visit(0, N, num, 0, 0, result)
print(min(result))