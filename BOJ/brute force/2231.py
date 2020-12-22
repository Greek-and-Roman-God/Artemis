N = int(input())

min = 1000000
for i in range(N-1, 0, -1) :
  temp = str(i)
  sum = 0
  for j in range(len(temp)) :
    sum += int(temp[j])
  if i + sum == N and i < min :
    min = i
print(min if min != 1000000 else 0)