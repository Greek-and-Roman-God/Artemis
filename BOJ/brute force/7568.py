N = int(input())

people = []
for _ in range(N) :
  #몸무게와 키를 튜플로 만들어 리스트에 담기
  people.append(tuple(map(int, input().split())))

result = []
for i in range(N) :
  cnt = 1
  for j in range(N) :
    #덩치가 작으면 순위에서 밀려난다 -> cnt += 1
    if people[i][0] < people[j][0] and people[i][1] < people[j][1] :
      cnt += 1
  result.append(cnt)

for i in result :
  print(i, end=' ')