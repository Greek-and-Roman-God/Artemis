#조금 더 나은 코드
dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
word = list(input())

result = 0
for i in word :
  for j in range(len(dial)) : 
    if i in dial[j] :
      result += j+3
      break
print(result)

"""
#처음 생각한 코드
word = list(input())
result = 0
for i in word :
  if ord(i) > ord("V") :
    result += 10
  elif ord(i) > ord("S") :
    result += 9
  elif ord(i) > ord("O") :
    result += 8
  elif ord(i) > ord("L") :
    result += 7
  elif ord(i) > ord("I") :
    result += 6
  elif ord(i) > ord("F") :
    result += 5
  elif ord(i) > ord("C") :
    result += 4
  else : 
    result += 3

print(result)
"""