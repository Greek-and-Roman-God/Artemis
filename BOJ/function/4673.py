def d(n) :
  n = n + sum(list(map(int, str(n))))
  return n

self_num = []
for i in range(1, 10000) :
  self_num.append(d(i))

for i in range(1, 10001) :
  if i not in self_num :
    print(i)