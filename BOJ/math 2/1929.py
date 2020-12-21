M, N = map(int, input().split())

prime_list = [True] * (N+1) #0 ~ N까지 저장
prime_list[0] = False #0은 소수가 아님
prime_list[1] = False #1은 소수가 아님

#에라토스테네스의 체를 이용
for i in range(2, int(N**0.5)+1) :
  if prime_list[i] :
    for j in range(i*2, len(prime_list), i) :
      prime_list[j] = False

for i in range(M, N+1) :
  if prime_list[i] :
    print(i)