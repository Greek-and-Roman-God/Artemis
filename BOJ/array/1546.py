import math

n = int(input())
list = list(map(int, input().split()))
m = max(list)

sum = 0
for i in list :
  i = i/m*100
  sum += i

print(round(sum/len(list), 2))