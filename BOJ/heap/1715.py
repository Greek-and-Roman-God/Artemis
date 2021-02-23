#Case 1
#		3
#	4 		5
#6

#3 + 4 = 7
#5 + 6 = 11
#7 + 11 = 18

#Case 2
#		10
#	10		20
#20		20

#10 + 10 = 20
#20 + 20 = 40
#20 + 20 = 40
#40 + 40 = 80

import heapq

N = int(input())

cards = []
for _ in range(N) :
  heapq.heappush(cards, int(input())) #최소 힙으로 구현

cnt = 0
#카드가 한 묶음인 경우 비교할 수 없으므로 건너뛴다
if not len(cards) == 1 :
  while len(cards) > 1 : #비교할 만큼의 카드 묶음이 있다면
    temp = heapq.heappop(cards) #제일 적은 묶음을 꺼낸다
    temp += heapq.heappop(cards) #그 다음 적은 묶음과 합친다
    heapq.heappush(cards, temp) #최소 힙의 알맞은 위치에 넣는다
    cnt += temp

print(cnt)