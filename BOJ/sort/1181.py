import sys

N = int(input())

words = []
for _ in range(N) :
  words.append(sys.stdin.readline().strip())

words = list(set(words))
words.sort(key=lambda x : (len(x), x))

for word in words :
  print(word)