n = input()
temp = n

cnt = 0
while True :
  if int(temp) < 10 :
    temp = "0" + temp
  first = temp[0]
  second = temp[1]
  sum = int(first) + int(second)
  temp = second + str(sum)
  if sum > 9 :
    temp = second + str(sum)[1]
  temp = str(int(temp))
  cnt += 1
  
  if n == temp :
    break


print(cnt)