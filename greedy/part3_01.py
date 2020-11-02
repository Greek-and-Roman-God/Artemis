n = int(input())
fearList = list(map(int, input().split()))
fearList.sort()

i = 0
cnt = 0
cntList = []

while i < len(fearList) :
  if fearList[i] == 1 :
    cnt += 1
    cntList.append(cnt)
    i += 1
  else :
    for j in range(i+1, len(fearList)) :
      if fearList[i] == fearList[j] : 
        cnt += 1
    cntList.append(cnt)
    i += cnt + 1
  cnt = 0

result = len(cntList) - cntList.count(0)
print(result)
  
  
