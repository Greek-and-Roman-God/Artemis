N = input()

mid = len(N) // 2
front = list(map(int, N[:mid]))
back = list(map(int, N[mid:]))

if sum(front) == sum(back) :
  print("LUCKY")
else :
  print("READY")