import sys
import math

N = int(input())
trees = []
for _ in range(N) :
  trees.append(int(sys.stdin.readline()))

#각 가로수들의 거리 차이를 저장
dist = []
for i in range(N-1) :
  dist.append(trees[i+1] - trees[i])

#거리들의 최대공약수를 구한다
#처음에는 최대거리와 최소거리의 최대공약수만 구했지만 30%쯤 실패해서 전체 거리의 최대공약수를 구함
interval = dist[0]
for i in dist :
  interval = math.gcd(interval, i)

#심어야하는 개수를 구한다
cnt = 0
for i in dist :
  cnt += i // interval - 1

print(cnt)