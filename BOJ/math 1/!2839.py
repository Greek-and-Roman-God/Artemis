#n>5일 때 나머지가 1이면 5를 하나 줄이고 3을 2개 추가, 나머지가 2이면, ... 이런 식으로 풀이하기
#혹은 5를 줄여가고 3을 늘이는 방식

#틀림
N = int(input())

cnt = 0
if (N % 5) % 3 == 0 :
  cnt = N//5 + (N%5)//3
elif N > 5 and ((N % 5) + 5) % 3 == 0 :
  cnt = ((N//5)-1) + (((N%5)+5)//3)
elif (N % 3) % 5 == 0 :
  cnt = N//3 + (N%3)//5
elif ((N % 3) + 3) % 5 == 0 :
  cnt = ((N//3)-1) + (((N%3)+3)//5)
else :
  cnt = -1

print(cnt)

"""
N = int(input())

a, b = N//5, 0
min = 5000
while not b > N//3 :
  if N//a
  cnt = a + b
  if cnt < min :
    min = cnt
  a -= 1
  b += 1

print(cnt)
"""