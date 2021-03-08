import sys
import heapq

N = int(input())
arr = []
for _ in range(N) :
  x = int(sys.stdin.readline())
  if x == 0 : #입력받은 숫자가 0인 경우
    if arr : #배열이 비어있지 않으면
      print(heapq.heappop(arr)[1])
    else :
      print(0)
  else :
    heapq.heappush(arr, (-x, x)) #최대 힙으로 구성