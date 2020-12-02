#find는 예외가 발생하면 -1을 반환함. if else 구문은 없어도 됨.

from sys import stdin
S = stdin.readline()
for i in range(ord('a'), ord('z')+1) :
  if chr(i) in S :
    print(S.find(chr(i)), end=' ')
  else :
    print(-1, end=' ')