N = int(input())

result = []
for _ in range(N) :
  result.append(tuple(map(int, input().split())))
result.sort()

for i in result :
  print(i[0], end=' ')
  print(i[1])