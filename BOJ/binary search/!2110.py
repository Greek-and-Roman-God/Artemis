#시간초과로 실패

from sys import stdin

n, c = map(int, stdin.readline().split())
x = []
for _ in range(n) :
  x.append(int(stdin.readline()))
x.sort()

left = 0
right = len(x)-1
c_list = []
while True :
  center = (left+right) // 2
  if left not in c_list :
    c_list.append(left)
    c -= 1
    if c == 0 :
      break
  if right not in c_list :
    c_list.append(right)
    c -= 1
    if c == 0 :
      break
  if center not in c_list :
    c_list.append(center)
    c -= 1
    if c == 0 :
      break
  if right - left == 3 :
    if x[center+1]-x[center] > x[right]-x[right-1] :
      left = center
    else :
      left = center + 1
  else :
    left = center
  if left > right :
    break

c_list.sort() #인덱스가 저장되어 있음
distance = 199999
for i in range(len(c_list)-1) :
  if x[c_list[i+1]] - x[c_list[i]] < distance :
    first = x[c_list[i]]
    second = x[c_list[i+1]]
    distance = second - first

print(distance)