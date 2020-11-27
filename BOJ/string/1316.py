from sys import stdin

N = int(stdin.readline())
result = 0
for i in range(N) :
  word = stdin.readline()
  for i in range(len(word)-1) :
    if word[i] != word[i+1] : #문자배열이 바뀌는 지점
      if word[i] in word[i+1:] : #이후로 해당 문자가 나온다면
        break
  else :
    result += 1

print(result)