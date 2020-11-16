#시간초과로 실패

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
m = int(input())
m_list = list(map(int, input().split()))

for i in m_list :
  low = 0
  high = len(n_list)-1
  cnt = 0
  while True : 
    center = (low + high) // 2
    if i > n_list[center] :
      low = center + 1
    elif i < n_list[center] :
      high = center - 1
    elif i == n_list[center] :
      cnt = n_list[low:high+1].count(i)
      break

    if low > high :
      break
  print(cnt, end=' ')