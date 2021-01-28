N = int(input())

#에라토스테네스의 체 생성
prime_check = [True] * (4000001)
for i in range(2, int(4000000**0.5)+1) :
  if prime_check[i] :
    for j in range(2*i, 4000001, i) :
      prime_check[j] = False

#소수 담기
prime_nums = [i for i in range(2, N+1) if prime_check[i]]

#투 포인터 활용
cnt = 0
end = 0
sum_prime = 2 #소수의 부분합. 첫 소수는 무조건 2
for start in prime_nums :
  #부분합이 N을 넘거나, 더이상 더할 소수가 없으면 빠져나옴
  while sum_prime < N and end < len(prime_nums) :
    end += 1
    if end == len(prime_nums) :
      break
    sum_prime += prime_nums[end]
  if sum_prime == N :
    cnt += 1
  sum_prime -= start #맨 앞의 수를 제거

print(cnt)