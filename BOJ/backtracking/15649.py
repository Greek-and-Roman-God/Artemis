from itertools import permutations

N, M = map(int, input().split())

nums = [i for i in range(1, N+1)]
result = permutations(nums, M)

for i in result :
  for j in range(M) :
    if j+1 != M :
      print(i[j], end=' ')
    else :
      print(i[j])