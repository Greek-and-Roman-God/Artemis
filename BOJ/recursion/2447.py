N = int(input())

def draw_star(star) :
  temp = []
  #한 줄씩 담는다
  for i in range(3 * len(star)) :
    if i // len(star) == 1 : #빈칸으로 표시할 부분
      temp.append(star[i % len(star)] + " " * len(star) + star[i % len(star)])
    else :
      temp.append(star[i % len(star)] * 3)
  return(temp)

cnt = 0 #재귀를 진행할 횟수
while N != 3 :
  N = N // 3
  cnt += 1

star = ["***", "* *", "***"] #기본 별찍기

#for문을 진행할 때마다 새로운 별찍기 리스트를 담는다
for _ in range(cnt) :
  star = draw_star(star)

for i in star :
  print(i)