T = int(input())

for _ in range(T) :
  k = int(input()) #층
  n = int(input()) #호
  
  #0층의 값
  #아래 for문에서 index 범위가 벗어나지 않도록 16으로 설정
  room = [i for i in range(1, 16)]

  for i in range(k) :
    for j in range(1, n+1) :
      room[j] = room[j-1] + room[j] #새로운 층의 값을 설정
  print(room[n-1])