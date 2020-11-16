n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
m = int(input())
m_list = list(map(int, input().split()))

for i in range(len(m_list)) :
  low = 0
  high = len(n_list)-1
  while True : 
    center = (low + high) // 2
    if m_list[i] > n_list[center] :
      low = center + 1
    elif m_list[i] < n_list[center] :
      high = center - 1
    elif m_list[i] == n_list[center] :
      print(1)
      break

    if low > high :
      print(0)
      break