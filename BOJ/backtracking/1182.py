N, S = map(int, input().split())
arr = list(map(int, input().split()))

visited = [False] * N
cnt = 0
result = []

def subseq(temp, depth, current) :
  global cnt
  if temp == depth :
    if sum(result) == S :
      cnt += 1
    return

  for i in range(current, N) :
    if not visited[i] :
      visited[i] = True
      result.append(arr[i])
      subseq(temp+1, depth, i)
      result.pop()
      visited[i] = False

for depth in range(1, N+1) : #부분수열의 길이를 1부터 N까지 늘려가면서 찾기
  subseq(0, depth, 0)
print(cnt)