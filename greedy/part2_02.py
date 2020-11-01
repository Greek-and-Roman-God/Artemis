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