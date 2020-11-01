n = int(input())
coinList = list(map(int, input().split()))
coinList.sort()

minVal = coinList[0]
maxVal = 0
for i in range(len(coinList)) :
  maxVal += coinList[i]

availList = []
temp = 0
for i in range(len(coinList)-1) :
  availList.append(coinList[i])
  for j in range(i+1, len(coinList)) :
    temp = availList[-1]
    temp += coinList[j]
    availList.append(temp)

result = 0
for i in range(minVal, maxVal+1) :
