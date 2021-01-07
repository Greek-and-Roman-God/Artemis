from itertools import combinations

N, M = map(int, input().split())

nums = [i for i in range(1, N+1)]
result = combinations(nums, M)

for i in result :
  print(' '.join(map(str, i)))