import sys

N = int(input())

members = []
for i in range(N) :
  members.append(list(sys.stdin.readline().split()))

#stable sort이기 때문에 그냥 정렬해도 가입 순으로 정렬된다
members.sort(key=lambda x : int(x[0]))

for member in members :
  print(member[0], end=' ')
  print(member[1])