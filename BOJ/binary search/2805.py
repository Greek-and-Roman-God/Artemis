#python3도 통과
N, M = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = max(trees)

result = []
while not right < left :
  length = 0
  mid = (left + right) // 2
  
  length = sum(i-mid if i > mid else 0 for i in trees)
  
  if length == M :
    result.append(mid)
    break
  elif length > M :
    result.append(mid)
    left = mid + 1
  else :
    right = mid - 1

print(max(result))

'''
#python3은 시간초과, pypy3은 통과
from sys import stdin

n, m = map(int, stdin.readline().split())
tree = list(map(int, stdin.readline().split()))

left = 0
right = max(tree)
result = 0

while not left > right :
  center = (left+right) // 2
  get = 0
  for i in tree :
    if i > center :
      get += i - center
  if get >= m : #나무길이를 딱 맞지 않게 가져가는 경우도 고려
    left = center + 1
    result = center
  elif get < m :
    right = center - 1

print(result)
'''