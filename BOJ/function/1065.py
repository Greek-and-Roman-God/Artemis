from sys import stdin

def han_num(n) :
  cnt = 0
  if n < 100 : #1 ~ 99는 무조건 등차수열
    cnt = n
    return cnt
  else :
    cnt = 99
  for i in range(100, n+1) :
    num = list(map(int, list(str(i))))
    temp = num[1] - num[0]
    for j in range(len(num)-1) :
      if temp != num[j+1] - num[j] :
        break
    else :
      cnt += 1
  return cnt

n = int(stdin.readline())
print(han_num(n))