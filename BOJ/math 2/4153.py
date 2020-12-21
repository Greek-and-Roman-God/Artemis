while True :
  num = list(map(int, input().split()))
  num.sort()
  if not num[2] : #0 0 0
    break

  if num[0]**2 + num[1]**2 == num[2]**2 :
    print('right')
  else :
    print('wrong')

"""
#처음 생각한 코드
while True :
  x, y, z = map(int, input().split())
  if not x and not y and not z : #0 0 0
    break
  
  if x**2 + y**2 == z**2 :
    print('right')
  elif x**2 + z**2 == y**2 :
    print('right')
  elif y**2 + z**2 == x**2 :
    print('right')
  else :
    print('wrong')
"""