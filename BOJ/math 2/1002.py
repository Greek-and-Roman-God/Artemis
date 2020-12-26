T = int(input())

for _ in range(T) :
  x1, y1, r1, x2, y2, r2 = map(int, input().split())
  dist = ((x1-x2)**2 + (y1-y2)**2)**(0.5)
  hap = r1 + r2
  cha = abs(r1 - r2)

  if x1 == x2 and y1 == y2 and r1 == r2 :
    print(-1)
  elif cha < dist and dist < hap :
    print(2)
  elif hap == dist :
    print(1)
  elif cha == dist :
    print(1)
  elif hap < dist :
    print(0)
  else : #dist < cha
    print(0)