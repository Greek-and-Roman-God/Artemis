import sys
import heapq

N, K = map(int, input().split())
gems = []
for _ in range(N) :
  heapq.heappush(gems, list(map(int, sys.stdin.readline().split())))
bags = [int(sys.stdin.readline()) for _ in range(K)]
bags.sort()

money = 0
temp = []
for bag in bags :
  while gems and gems[0][0] <= bag : #보석이 남아있고, 가방의 무게보다 적은 보석이라면 전부 가격을 temp에 담는다
    heapq.heappush(temp, -heapq.heappop(gems)[1]) #최대 힙을 구성하므로 -를 붙여준다
  if temp : #temp에 하나라도 있으면 하나를 빼서 가격을 더해준다
    #이 때 보석 하나를 빼고도 temp에 남아있는 보석은 다음 가방에 담기게 된다
    money -= heapq.heappop(temp) #최대 힙으로 구성된 것이므로 다시 -를 붙여준다
  elif not gems : #보석이 남아있지 않으면 멈춘다
    break

print(money)