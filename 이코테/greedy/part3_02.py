#210421
S = input()

result = int(S[0]) #첫 번째 자리를 미리 저장
for i in range(1, len(S)) :
  if not int(S[i-1]) or not int(S[i]) : #0인 경우 더하고 0이 아니면 곱함
    result += int(S[i])
  else :
    result *= int(S[i])

print(result)

#201111
s = input()
result = int(s[0])

for i in range(len(s)-1) :
  if s[i] == '0' or s[i+1] == '0' :
    result = result + int(s[i+1])
  else :
    result = result * int(s[i+1])

print(result)