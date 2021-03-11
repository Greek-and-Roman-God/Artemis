import heapq

N = int(input())
station = [list(map(int, input().split())) for _ in range(N)]
length, oil = map(int, input().split())

station.sort() #가까운 순으로 정렬
stop = [] #멈출 주유소
cnt = 0 #멈추는 횟수
while oil < length :
  while station and oil >= station[0][0] : #주유소가 남아있고, 현재 보유한 연료로 갈 수 있다면
    s = heapq.heappop(station)
    heapq.heappush(stop, (-s[1], s[0])) #연료를 많이 주는 순으로 최대 힙 구성
  
  if not stop : #갈 수 있는 주유소가 없다면
    cnt = -1
    break

  s = heapq.heappop(stop) #갈 수 있는 곳 중 가장 연료를 많이 주는 곳으로 간다
  oil += -s[0] #연료를 계속 누적해서 마을까지의 거리와 비교한다
  cnt += 1

print(cnt)