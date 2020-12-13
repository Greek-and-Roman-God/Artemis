N = int(input())

x = N // 5 #5kg 봉지 개수
y = (N % 5) // 3 #3kg 봉지 개수

cnt = -1 #값이 안 나올 때
while x > -1 :
   if not 5*x + 3*y == N :
    x -= 1 #5kg 봉지를 줄이고
    y = (N - (5*x)) // 3 #가능한만큼 3kg 봉지를 늘린다
   else :
    cnt = x + y
    break

print(cnt)