N = int(input())
students = [list(input().split()) for _ in range(N)]
students.sort(key=lambda x : x[1])

for i in range(N) :
  print(students[i][0], end=' ')