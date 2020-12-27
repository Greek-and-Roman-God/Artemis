#자리수 * 9를 N에서 빼준 값부터 찾기 시작하면 훨씬 빨라짐

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