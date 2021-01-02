import sys

N = int(input())

members = []
for i in range(N) :
  members.append(list(sys.stdin.readline().split()))
  members[i].append(i)

members.sort(key=lambda x : (int(x[0]), x[2]))

for member in members :
  print(member[0], end=' ')
  print(member[1])