T = int(input())
for _ in range(T) :
  N, M = map(int, input().split())
  req = [list(map(int, input().split())) for _ in range(M)]
  req = sorted(req, key=lambda x : x[1]) #신청서의 두 번째 정수가 작은 순으로 정렬

  cnt = 0
  visited = [False] * (N+1) #책 나눠준 여부 체크
  for a, b in req : #각 학생 별로
    for i in range(a, b+1) : #신청한 책을 돌면서
      if not visited[i] : #아직 안 나눠준 책이라면 나눠준다
        visited[i] = True
        cnt += 1
        break

  print(cnt)