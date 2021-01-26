import sys

T = int(input())

case = []
for _ in range(T) :
  case.append(list(map(int, sys.stdin.readline().split())))

#두 끈의 길이가 최대치인 2*10^12 * 2라고 생각하고
#그것의 root값까지만 구해준다. 최대치까지 구하면 메모리초과가 남
prime_flag = [True] * 2000001

for i in range(2, int(2000000**0.5)+1) :
  if prime_flag[i] :
    for j in range(2*i, 2000001, i) :
      prime_flag[j] = False

for (a,b) in case :
  length = a + b
  if length < 4 : #4보다 작은 수는 소수로 나눌 수 없다
    print("NO")
  elif not length % 2 : #골드바흐의 추측 (4보다 큰 짝수)
    print("YES")
  else : #4보다 큰 홀수일 경우
    length -= 2 #끈의 길이를 2와 어떤 수로 나눈다고 가정 
    for i in range(2, len(prime_flag)) :
      if prime_flag[i] :
        if i * i > length :
          print("YES")
          break
        if not length % i : #소수로 나눠지면 소수가 아니다
          print("NO")
          break
    else :
      print("YES")