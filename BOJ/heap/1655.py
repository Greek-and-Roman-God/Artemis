import heapq
import sys

N = int(input())
min_heap, max_heap = [], []

for _ in range(N) :
  num = int(sys.stdin.readline())
  if len(min_heap) == len(max_heap) :
    heapq.heappush(max_heap, (-num, num)) #-num을 이용해 최대 힙으로 구성
  else :
    heapq.heappush(min_heap, (num, num)) #최소 힙

  if min_heap and max_heap[0][1] > min_heap[0][1] : #순서가 뒤바뀐 경우
    max_val = heapq.heappop(max_heap)[1]
    min_val = heapq.heappop(min_heap)[1]
    heapq.heappush(max_heap, (-min_val, min_val))
    heapq.heappush(min_heap, (max_val, max_val))
  
  print(max_heap[0][1])