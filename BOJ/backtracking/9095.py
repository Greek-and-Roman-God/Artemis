import sys

ott = [1,2,3]

def plus(current) : #current는 현재 인덱스
  global cnt, result
  
  #결과값이 크면 다음 인덱스로 갈 필요가 없으므로 return
  if result >= n :
    if result == n : #같으면 cnt를 증가시킨 후 return
      cnt += 1
    return

  #결과값이 작으면 ott의 처음 값부터 다시 더한다
  #i가 증가하면서 다음 인덱스의 값이 더해진다
  for i in range(len(ott)) :
    result += ott[i]
    plus(i)
    result -= ott[i]

T = int(input())
for _ in range(T) :
  n = int(sys.stdin.readline())
  cnt, result = 0, 0 #케이스를 돌 때마다 초기화 시켜준다
  plus(0)
  print(cnt)