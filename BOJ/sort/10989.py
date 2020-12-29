import sys

N = int(input())

#범위를 지정해서 메모리 초과가 일어나지 않도록 해야 한다
n_list = [0] * 10001
for _ in range(N) :
  n_list[int(sys.stdin.readline())] += 1

for i in range(1, len(n_list)) :
  for j in range(n_list[i]) :
    print(i)



#실패
#카운팅 정렬을 시도했으나 메모리 초과로 전부 실패함
"""
#메모리 초과2
import sys

N = int(input())

n_list = [0] * 10001
for _ in range(N) :
  n_list[int(sys.stdin.readline())] += 1

for i in range(len(n_list)-1) :
  n_list[i+1] += n_list[i]

result = [0] * N
for i in range(len(n_list)-1, 0, -1) :
  result[n_list[i]-1] = i
  for j in range(1, n_list[i]+1) :
    result[n_list[i]-j] = i

for i in result :
  print(i)
"""

"""
#메모리 초과
import sys

N = int(input())

n_list = []
for _ in range(N) :
  n_list.append(int(sys.stdin.readline()))

cnt_list = [0] * (max(n_list)+1)
for i in n_list :
  cnt_list[i] += 1

for i in range(len(cnt_list)-1) :
  cnt_list[i+1] += cnt_list[i]

result = [0] * N
for i in range(N-1, -1, -1) :
  result[cnt_list[n_list[i]]-1] = n_list[i]
  cnt_list[n_list[i]] -= 1

for i in result :
  print(i)
"""