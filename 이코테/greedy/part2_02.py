#210319
N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

result = arr[0] #제일 큰 수를 result에 저장
for i in range(1, M) :
  if i % K : #K번까지는 제일 큰 수를 더하고
    result += arr[0]
  else : #그 이후 한 번은 그 다음으로 큰 수를 더해준다
    result += arr[1]

print(result)

#201111
n, m, k = map(int, input().split())
list = list(map(int, input().split()))

first = 0
second = 0
firstIndex = 0

for i in range(len(list)) :
  if list[i] > first :
    first = list[i]
    firstIndex = i
for i in range(len(list)) :
  if list[i] > second and i != firstIndex :
    second = list[i]

result = 0
cnt = 0
flag = True
while flag:
  for i in range(k):
    if cnt < m :
      result += first
      cnt += 1
    else : 
      flag = False
      break
  if cnt < m :
    result += second
    cnt += 1
  else :
    flag = False

print(result)