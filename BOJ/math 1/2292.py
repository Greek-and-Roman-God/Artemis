N = int(input())

cnt = 1 #지나온 방의 개수
num = 1 #방의 끝번호 1, 7, 19, ...
while True :
  if N <= num :
    print(cnt)
    break
  num += 6 * cnt #방의 끝번호 차이는 6, 12, 18, ... 계차수열
  cnt += 1