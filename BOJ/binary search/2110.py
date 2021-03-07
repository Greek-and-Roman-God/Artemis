import sys

N, C = map(int, input().split())
home = [int(sys.stdin.readline()) for _ in range(N)]
home.sort()

left = 1
right = home[-1] - home[0]
while not right < left :
  mid = (left + right) // 2
  cnt = 1
  temp = home[0] #공유기를 설치한 집
  for i in range(1, N) : #집을 돌면서
    if temp + mid <= home[i] : #앞서 공유기를 설치한 집과 기준 거리(제일 인접한 거리) 이상이면
      temp = home[i] #공유기를 설치한다
      cnt += 1
  
  if cnt >= C :
    result = mid
    left = mid + 1
  else :
    right = mid - 1

print(result)