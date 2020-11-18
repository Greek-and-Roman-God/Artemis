#시간초과로 실패

"""
스터디
1.처음에 들어오는 값을 딕셔너리로 처리해보는 방법 생각해보기
2.처음에 들어오는 값을 set으로 만들어 중복을 없앤 후 거기서 이진탐색을 해보기
"""

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