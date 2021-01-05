N = int(input())

temp = 2
while not N == 1 :
  if N % temp == 0 :
    print(temp)
    N = N // temp
  else :
    temp += 1