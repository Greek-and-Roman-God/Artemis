X = int(input())

max_num = 0 #분자 또는 분모가 될 수 있는 최대의 수
cnt = 0 #n번째 수
a, b = 0, 0 #분자, 분모
temp = 1

while True :
  if cnt >= X :
    move = cnt % X #나머지만큼 이동해야 함
    break
  max_num += 1
  cnt += temp
  temp += 1

if max_num % 2 == 0 : #짝수줄일 경우 분자 -이동, 분모 +이동
  a = max_num - move
  b = 1 + move
else : #홀수줄일 경우 분자 +이동, 분모 -이동
  a = 1 + move
  b = max_num - move

print(f'{a}/{b}')