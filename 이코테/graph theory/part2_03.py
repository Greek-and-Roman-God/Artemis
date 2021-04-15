import sys

def find_parent(parent, x) :
  if parent[x] != x :
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union(parent, a, b) :
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b :
    parent[b] = a
  else :
    parent[a] = b

N, M = map(int, input().split())
parent = [i for i in range(N+1)]

graph = []
for _ in range(M) :
  a, b, c = map(int, sys.stdin.readline().split())
  graph.append((c, a, b))
graph.sort()

cost = 0
remove_cost = 0
for c, a, b in graph :
  if find_parent(parent, a) != find_parent(parent, b) :
    union(parent, a, b)
    cost += c
    remove_cost = c

print(cost - remove_cost)