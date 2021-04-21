#210422
N, M = map(int, input().split())
ball = list(map(int, input().split()))

result = 0
for i in range(N) :
  for j in range(i+1, N) :
    if ball[i] != ball[j] and ball[i] <= M and ball[j] <= M : #최대 무게를 넘지 않는 공이고, 같은 무게가 아니라면
      result += 1

print(result)

#201111
n, m = map(int, input().split())
wList = list(map(int, input().split()))

cnt = 0
for i in range(len(wList)-1) :
  for j in range(i+1, len(wList)) :
    if wList[i] != wList[j] :
      cnt += 1

print(cnt)