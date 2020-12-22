N, M = map(int, input().split())
n = list(map(int, input().split()))
n.reverse()

max = 0
for i in range(N-1) :
  for j in range(i+1, N) :
    for k in range(j+1, N) :
      if max < n[i]+n[j]+n[k] and n[i]+n[j]+n[k] <= M :
        max = n[i] + n[j] + n[k]
print(max)