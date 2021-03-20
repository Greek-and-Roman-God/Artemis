#210320
now = input()
row, col = now[1], now[0]

#이동 가능한 방향
move = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

cnt = 0
for x, y in move :
  #범위를 벗어나면 다음 방향으로 넘어간다
  if int(row) + x < 1 or int(row) + x > 8 or ord(col) + y < ord("a") or ord(col) + y > ord("h") : continue
  cnt += 1

print(cnt)


#201111
now = input() #a1
x = now[0] #a
y = now[1] #1

cnt = 0
#왼쪽 수평 2칸 이동
if x > 'b' :
  if int(y) > 1 :
    cnt += 1
  if int(y) < 8 :
    cnt += 1
#오른쪽 수평 2칸 이동
if x < 'g' :
  if int(y) > 1 :
    cnt += 1
  if int(y) < 8 :
    cnt += 1
#위쪽 수직 2칸 이동
if int(y) > 2 :
  if x > 'a' :
    cnt += 1
  if x < 'h' :
    cnt += 1
#아래쪽 수직 2칸 이동
if int(y) < 7 :
  if x > 'a' :
    cnt += 1
  if x < 'h' :
    cnt += 1

print(cnt)