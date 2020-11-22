from sys import stdin

k, n = map(int, stdin.readline().split())
K = []
for _ in range(k) :
  K.append(int(stdin.readline()))

start = 1
end = max(K) #모든 랜선이 잘려야하는 것은 아니다
max = 0
while not start > end :
  cnt = 0
  center = (start+end)//2
  for i in range(len(K)) :
    cnt += K[i]//center
  if cnt < n :
    end = center - 1
  elif cnt >= n :
    max = center
    start = center + 1
print(max)