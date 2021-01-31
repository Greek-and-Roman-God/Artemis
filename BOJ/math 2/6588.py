import sys

prime_flag = [True] * (1000001)

for i in range(2, int(1000000**0.5)+1) :
  if prime_flag[i] :
    for j in range(2*i, 1000001, i) :
      prime_flag[j] = False

while True :
  n = int(sys.stdin.readline())
  if not n :
    break
  for i in range(2, len(prime_flag)) :
    if prime_flag[i] and prime_flag[n-i] :
      print(f'{n} = {i} + {n-i}')
      break