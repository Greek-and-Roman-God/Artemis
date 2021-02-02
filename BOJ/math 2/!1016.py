#시간초과
MIN, MAX = map(int, input().split())

n = 1000000
prime_check = [True] * (n+1)
for i in range(2, int(n**0.5)+1) :
  if prime_check[i] :
    for j in range(i*i, n+1, i*i) :
      prime_check[j] = False
non_prime = [i for i in range(n+1) if not prime_check[i]]

cnt = MAX - MIN + 1
for i in range(MIN, MAX+1) :
  if i < 1000001 :
    if i in non_prime :
      cnt -= 1
  else :
    for j in non_prime :
      if not i % j :
        cnt -= 1
        break
print(cnt)