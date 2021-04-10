#개선된 다익스트라 알고리즘 사용
import heapq

INF = int(1e9) #무한을 나타내는 변수
N, M, C = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M) :
  X, Y, Z = map(int, input().split())
  graph[X].append((Y, Z))

distance = [INF] * (N+1) #각 도시에 전보를 보내는 시간을 무한으로 설정

queue = []
heapq.heappush(queue, (0, C)) #전보를 보내는 도시는 C, 자기 자신과의 시간은 0
distance[C] = 0
while queue :
  dist, now = heapq.heappop(queue)
  if distance[now] < dist : continue #이미 처리된 도시라면 건너뛴다
  for i in graph[now] : #통로가 있는 곳을 돌면서
    cost = dist + i[1]
    if cost < distance[i[0]] : #현재 설정된 시간보다 시간이 적게 든다면 재설정
      distance[i[0]] = cost
      heapq.heappush(queue, (cost, i[0]))

cnt = 0 #전보를 보낼 수 있는 도시의 총 개수
total_time = 0 #전보를 보내는 총 시간
for i in range(1, N+1) :
  if distance[i] != INF and distance[i] : #통로가 존재하고, 자기 자신이 아니라면
    cnt += 1
    total_time = max(total_time, distance[i]) #제일 오래 걸린 시간이 전보를 보내는 총 시간

print(cnt, end=' ')
print(total_time)