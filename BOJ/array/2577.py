a = int(input())
b = int(input())
c = int(input())

result = str(a*b*c)

cnt_list = [None] * 10

for i in range(10) :
  cnt = 0
  for j in range(len(result)) :
    if result[j] == str(i) :
      cnt += 1
  cnt_list[i] = cnt

for i in cnt_list :
  print(i)