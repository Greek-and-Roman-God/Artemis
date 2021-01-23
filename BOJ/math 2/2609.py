A, B = map(int, input().split())

gcf = 1

temp = 2
while temp <= min(A, B) :
  if not A % temp and not B % temp : #둘 다 temp로 나누어 떨어지면
    A //= temp
    B //= temp
    gcf *= temp
  else :
    temp += 1

print(gcf) #최대공약수
print(gcf * A * B) #최소공배수