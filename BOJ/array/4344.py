c = int(input())

for i in range(c) :
  cnt = 0
  data = list(map(int, input().split()))
  avg = sum(data[1:])/data[0]
  for j in range(1, len(data)) :
    if data[j] > avg :
      cnt += 1
  temp = cnt/data[0]*100
  print("%0.3f%%" % temp)