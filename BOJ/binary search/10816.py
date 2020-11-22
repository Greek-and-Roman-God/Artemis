#이진탐색으로 탐색범위를 줄이고 딕셔너리를 활용하는 것이 정석같음
from sys import stdin

#들어오는 값을 딕셔너리로 처리
n = int(stdin.readline())
n_list = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
m_list = list(map(int, stdin.readline().split()))

n_dict = {}
for i in n_list :
  if i not in n_dict :
    n_dict[i] = 1
  else :
    n_dict[i] += 1

for i in m_list :
  if i in n_dict :
    print(n_dict[i], end=' ')
  else :
    print(0, end=' ')

"""
#시간초과
#들어오는 값을 set으로 만들어 중복을 없앤 후 이진탐색
n = int(stdin.readline())
n_list = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
m_list = list(map(int, stdin.readline().split()))

n_set = list(sorted(set(n_list)))

for i in m_list :
  low = 0
  high = len(n_set)-1
  cnt = 0
  while True : 
    center = (low + high) // 2
    if i > n_set[center] :
      low = center + 1
    elif i < n_set[center] :
      high = center - 1
    elif i == n_set[center] :
      cnt = n_list.count(i)
      break

    if low > high :
      break
  print(cnt, end=' ')
"""