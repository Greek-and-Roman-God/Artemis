#틀림

#실수 연산에는 오차가 발생. sqrt x == y 대신 x==y*y 이용

import decimal

T = int(input())

for _ in range(T) :
  x1, y1, r1, x2, y2, r2 = map(int, input().split())
  dist = decimal.Decimal(((x1-x2)**2 + (y1-y2)**2) ** 0.5)
  hap = decimal.Decimal(r1) + decimal.Decimal(r2)
  cha = decimal.Decimal(max(r1, r2))-decimal.Decimal(min(r1, r2))

  if x1 == y1 and x2 == y2 :
    if r1 == r2 :
      print(-1)
    else :
      print(0)
  else :
    if cha < dist and dist < hap :
      print(2)
    elif hap == dist :
      print(1)
    elif cha == dist :
      print(1)
    elif hap < dist :
      print(0)
    else : #dist < cha :
      print(0)