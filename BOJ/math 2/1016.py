import math
MIN, MAX = map(int, input().split())

#제곱ㄴㄴ수를 체크할 배열
square_chk = [1 for _ in range(MIN, MAX+1)]

#MAX보다 작은 제곱수를 저장
square = [i**2 for i in range(2, int(MAX**0.5)+1)]
for i in square :
  #제곱수에 해당하는 인덱스(sqaure_chk의 인덱스)를 구하는 과정
  #math.ceil(MIN/i)*i -> MIN보다 큰 최소의 제곱수의 배수
  #-MIN -> 인덱스를 구하기 위해 MIN을 뺌
  temp = (math.ceil(MIN / i) * i) - MIN
  while temp <= MAX - MIN : #인덱스를 벗어나지 않도록
    square_chk[temp] = 0 #제곱수의 배수는 0으로 변경
    temp += i #제곱수의 배수를 걸러내기 위해 i를 계속 더해줌

print(sum(square_chk))