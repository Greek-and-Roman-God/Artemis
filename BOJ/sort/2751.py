import sys

N = int(input())

result = []
for _ in range(N) :
  result.append(int(sys.stdin.readline()))

result.sort()
for i in result :
  print(i)