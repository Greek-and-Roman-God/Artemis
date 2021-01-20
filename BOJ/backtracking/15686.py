import sys

N, M = map(int, input().split())
city = []
chickens = []
home = []
for i in range(N) :
  city.append(list(map(int, sys.stdin.readline().split())))
  #한 줄씩 읽어들이면서 집과 치킨집의 위치를 저장
  for j in range(N) :
    if city[i][j] == 2 :
      chickens.append((i+1,j+1))
    elif city[i][j] == 1 :
      home.append((i+1,j+1))

visited = [False] * len(chickens)
distance = [] #치킨 거리들
survive = [] #폐업하지 않고 살아남은 치킨집
def remove(depth, current) :
  if depth == M :
    dist_tmp = 0 #현재 남은 치킨집에 대한 치킨 거리
    for i in range(len(home)) :
      temp = 2e9
      #각 집에 대해 치킨집들 중 가장 가까운 거리를 temp에 저장
      for j in range(len(survive)) :
        temp = min(temp, abs(home[i][0]-survive[j][0])+abs(home[i][1]-survive[j][1]))
      dist_tmp += temp
    distance.append(dist_tmp)
    return
  
  #current 변수가 없으면 중복탐색으로 인해 시간초과가 발생
  for i in range(current, len(visited)) :
    if not visited[i] :
      visited[i] = True
      survive.append(chickens[i])
      remove(depth+1, i)
      survive.pop()
      visited[i] = False

remove(0, 0)
print(min(distance)) #치킨 거리들 중 최소값 출력