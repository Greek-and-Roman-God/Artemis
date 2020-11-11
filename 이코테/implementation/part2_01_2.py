n = int(input())

h, m, s = 0, 0, 0

cnt = 0
while not h == n+1 :
  if '3' in str(h) or '3' in str(m) or '3' in str(s) :
    cnt += 1
  s += 1
  if s == 60 :
    s = 0
    m += 1
  if m == 60 :
    m = 0
    h += 1

print(cnt)