n = int(input())

for i in range(n) :
  cnt = 0
  data = input()
  temp = 1
  for j in range(len(data)) :
    if data[j] == "X" :
      temp = 1
      continue
    else : 
      cnt += temp
      temp += 1
  print(cnt)