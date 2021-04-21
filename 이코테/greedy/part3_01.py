#210421
N = int(input())
guild = list(map(int, input().split()))
guild.sort() #공포도 순으로 정렬

result = 0 #여행을 떠날 그룹 수
tmp = 0 #각 그룹의 인원
for i in guild :
  fear = i #높은 공포도를 가진 사람이 있으면 공포도를 변경
  tmp += 1
  if fear == tmp : #공포도와 인원 수가 일치하면 여행을 떠남
    result += 1
    tmp = 0

print(result)

#201111
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
  
  
