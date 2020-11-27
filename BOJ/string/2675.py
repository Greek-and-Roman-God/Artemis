from sys import stdin
T = int(stdin.readline())
for _ in range(T) :
  R, S = stdin.readline().split()
  for i in S :
    print(int(R)*i, end='')
  print()