#210319
N, K = map(int, input().split())

cnt = 0
while not N == 1 :
  if N % K :
    N -= 1
  else :
    N //= K
  cnt += 1

print(cnt)

#201111
n, k = map(int, input().split())
cnt = 0

while n > 1 :
  cnt += 1
  if n % k == 0 :
    n = n/k
  else :
    n = n-1

print(cnt)