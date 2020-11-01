s = input()
result = int(s[0])

for i in range(len(s)-1) :
  if s[i] == '0' or s[i+1] == '0' :
    result = result + int(s[i+1])
  else :
    result = result * int(s[i+1])

print(result)