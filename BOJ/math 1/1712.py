#처음 생각한 코드 (시간 오래 걸림)
from sys import stdin

A, B, C = map(int, stdin.readline().split())

def sell() :
  cnt = 1
  revenue = C - B #노트북 판매 대수에 따른 이익
  if not revenue > 0 :
    return -1 
  while True :
    if cnt * revenue > A :
      break
    else :
      cnt += 1
  return cnt

print(sell())

"""
#좀 더 나은 코드 (while문을 돌리지 않아도 됨))
A, B, C = map(int, stdin.readline().split())
if C <= B :
  print(-1)
else :
  print(A//(C-B) + 1)
"""