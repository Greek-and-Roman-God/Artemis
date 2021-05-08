import sys

N = int(input())
arr = []
for _ in range(N) :
  name, kor, eng, math = sys.stdin.readline().split()
  arr.append([name, kor, eng, math])

arr = sorted(arr, key=lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in arr :
  print(i[0])