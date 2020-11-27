from sys import stdin

word = list(stdin.readline().rstrip().lower()) #소문자로 변환
char = [0] * 26 #a-z의 개수를 저장할 리스트

for i in word :
  char[ord(i)-97] += 1

if char.count(max(char)) > 1 : 
  print('?')
else :
  print(chr(char.index(max(char))+65)) #대문자로 출력