#에라토스테네스의 체를 미리 생성 (제한은 10000이하)
prime_list = [True] * 10001 #0 ~ 10000 인덱스
prime_list[0] = False
prime_list[1] = False

for i in range(2, int(10000**0.5)+1) :
  if prime_list[i] :
    for j in range(i*2, 10001, i) :
      prime_list[j] = False

T = int(input())

for _ in range(T) :
  n = int(input())
  min = 10000
  for i in range(n//2+1) :
    if prime_list[i] : #소수라면
      x, y = i, n - i
      #y도 소수인지, 최소값인지 판별
      if prime_list[y] and y-x <= min :
        min = y - x
        first, second = x, y
  print(f'{first} {second}')