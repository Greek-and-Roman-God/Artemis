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