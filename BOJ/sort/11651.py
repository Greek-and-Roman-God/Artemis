N = int(input())

result = []
for _ in range(N) :
  result.append(tuple(map(int, input().split())))
result.sort(key = lambda x : (x[1],x[0])) #정렬 조건설정

for i in result :
  print(i[0], end=' ')
  print(i[1])