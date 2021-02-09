import sys

T = int(input())
for _ in range(T) :
  N = int(sys.stdin.readline())
  if N == 0 :
    print('1 0')
  elif N == 1 :
    print('0 1')

  #0과 1의 개수는 앞에 나온 0과 1의 개수를 저장해서 활용한다
  a_zero, a_one = 1, 0 #0을 호출할 경우
  b_zero, b_one = 0, 1 #1을 호출할 경우
  for now in range(2, N+1) : #2를 호출할 경우부터 돌아간다
    now_zero = a_zero + b_zero
    now_one = a_one + b_one
    if now == N :
      print(f'{now_zero} {now_one}')
      break

    a_zero, a_one = b_zero, b_one
    b_zero, b_one = now_zero, now_one