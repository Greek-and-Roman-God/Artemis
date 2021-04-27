S = input()

char = ""
num = 0
for i in S :
  if "0" <= i and  i <= "9" : #숫자면 num에 더하고 문자면 char에 더함
    num += int(i)
  else :
    char += i

char = list(char)
char.sort()
print("".join(char), end='')
print(num if num else '') #숫자가 0이 아니면 맨 뒤에 출력