N = int(input())

def move(N, start, end) :
  if N > 1 :
    move(N-1, start, 6-start-end) #6-start-end -> 중간기둥
  print(start, end=' ')
  print(end)
  if N > 1 :
    move(N-1, 6-start-end, end)

print(2**N - 1) #이동횟수
move(N, 1, 3)