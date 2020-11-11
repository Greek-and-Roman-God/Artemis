n = int(input())
plan = list(input().split())

x = 1
y = 1

for i in plan :
  if i == "L" and y != 1 :
    y -= 1
    continue
  if i == "R" and y != n-1 :
    y += 1
    continue
  if i == "U" and x != 1 :
    x -= 1
    continue
  if i == "D" and x != n-1 :
    x += 1
    continue

print("%d %d" % (x, y))