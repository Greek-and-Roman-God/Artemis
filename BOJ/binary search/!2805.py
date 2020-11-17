#시간초과, 답도 나오지 않음

from sys import stdin

n, m = map(int, stdin.readline().split())
sum = 0
tree = list(map(int, stdin.readline().split()))
for i in range(n) :
  sum += tree[i]
tree.sort()

for h in range(1, sum+1) : #나무 높이의 합은 항상 M을 넘는다
  left = 0
  right = len(tree)-1
  get = 0
  while True :
    if left > right :
      break
    center = (left+right) // 2
    if tree[center] == h or tree[center] < h < tree[center+1 if center != len(tree)-1 else center] :
      for i in range(center+1, len(tree)) :
        tree[i] -= h
        get += h
      break
    elif tree[center] > h :
      right = center-1
    elif tree[center] < h :
      left = center+1
  if get == m :
    break

print(get)