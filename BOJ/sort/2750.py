#sort 사용O
N = int(input())

result = []
for _ in range(N) :
  result.append(int(input()))

result.sort()
for i in result :
  print(i)

#sort 사용X
N = int(input())

result = []
for _ in range(N) :
  result.append(int(input()))

for i in range(len(result)-1) :
  for j in range(i, len(result)) :
    if result[i] > result [j] :
      result[i], result[j] = result[j], result[i]

for i in result :
  print(i)