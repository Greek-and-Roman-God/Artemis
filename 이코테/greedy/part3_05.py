n, m = map(int, input().split())
wList = list(map(int, input().split()))

cnt = 0
for i in range(len(wList)-1) :
  for j in range(i+1, len(wList)) :
    if wList[i] != wList[j] :
      cnt += 1

print(cnt)