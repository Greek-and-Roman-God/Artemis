#210319
N, M = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(N) :
  result = max(min(cards[i]), result) #각 행의 가장 작은 숫자 중 큰 숫자를 저장

print(result)

#201111
n, m = map(int, input().split())
data = [0] * m
temp = []

for i in range(n) :
  temp = list(map(int, input().split()))
  temp.sort()
  data[i] = temp[0]

data.sort()
print(data[-1])