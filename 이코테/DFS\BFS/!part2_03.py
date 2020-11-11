n, m = map(int, input().split())
#frame = [[]]
frame = []
cnt = 0
cnt_list = []

def count_ice(frame, start, visited) :
  for i in range(len(frame[start])) :
    if visited[start][i] == False :
      visited[start][i] = True
      if frame[start][i] == '0' :
        count_ice(frame, start+1, visited)

for i in range(n) :
  temp = []
 # temp.append([])
  input_data = input()
  for j in range(len(input_data)) :
    temp.append(input_data[j:j+1])
  frame.append(temp)

visited = [[False]*m] * n

count_ice(frame, 0, visited)

print(frame)
print(visited)
print(len(cnt_list))