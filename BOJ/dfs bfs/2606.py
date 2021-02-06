N = int(input()) #컴퓨터의 수
K = int(input()) #연결되어 있는 컴퓨터 쌍의 수

#인접행렬 생성
network = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(K) :
 link = list(map(int, input().split()))
 network[link[0]-1][link[1]-1] = 1
 network[link[1]-1][link[0]-1] = 1

visited = [False] * N #방문여부 체크
cnt = 0
def virus(cur, network, visited) :
  global cnt

  if not visited[cur] : #바이러스 체크하지 않은 곳
    visited[cur] = True
    for i in range(N) :
      if network[cur][i] == 1 and not visited[i]:
        cnt += 1
        virus(i, network, visited)

virus(0, network, visited)
print(cnt)