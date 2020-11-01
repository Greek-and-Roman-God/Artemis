n, m = map(int, input().split())
data = [0] * m
temp = []

for i in range(n) :
  temp = list(map(int, input().split()))
  temp.sort()
  data[i] = temp[0]

data.sort()
print(data[-1])