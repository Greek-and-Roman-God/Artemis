N = int(input())
request = list(map(int, input().split()))
M = int(input())

left = M // N
right = max(request)

result = []
while not right < left :
  budget = 0
  mid = (left + right) // 2
  for i in request :
    if i <= mid :
      budget += i #요청액이 상한액보다 적은 경우 요청액을 배정
    else :
      budget += mid #요청액이 상한액보다 많은 경우 상한액을 배정
  if M - budget < 0 : #예산 범위를 넘어가면 상한액을 줄인다
    right = mid - 1
  else :
    result.append(mid) #예산 범위 안에 들어가면 상한액을 저장한다
    left = mid + 1

print(max(result))