T = int(input())

for _ in range(T) :
  H, W, N = map(int, input().split())

  if N % H == 0 : #꼭대기층에 배정받는 경우
    floor = str(H)
    room = N // H
  else :
    floor = str(N % H)
    room = (N // H) + 1

  if room < 10 :
    room = '0' + str(room)
  else :
    room = str(room)

  print(floor + room)