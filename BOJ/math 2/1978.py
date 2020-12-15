N = int(input())
n_list = list(map(int, input().split()))

cnt = 0
for n in n_list :
  if n != 1 : #1은 소수가 아님
    for i in range(2, n) :#1과 자기자신을 제외한 수로 나뉘면 X
      if n % i == 0 :
        break
    else :
      cnt += 1

print(cnt)