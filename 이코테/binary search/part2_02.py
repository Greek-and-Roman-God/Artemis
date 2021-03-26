N = int(input())
have = list(map(int, input().split()))
M = int(input())
request = list(map(int, input().split()))

have.sort()
for req in request : #손님이 찾는 물품별로 이진탐색
  left = 0
  right = N-1
  while True :
    mid = (left + right) // 2
    if have[mid] == req :
      print("yes", end=" ")
      break
    elif have[mid] > req :
      right = mid - 1
    elif have[mid] < req :
      left = mid + 1
    if left > right :
      print("no", end=" ")
      break