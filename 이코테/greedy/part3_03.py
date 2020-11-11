s = input()
zCnt = s.count('0')
oCnt = s.count('1')

result = len(s.split('1'))-s.split('1').count('') + len(s.split('0'))-s.split('0').count('')

if zCnt > oCnt :
  result = result - (len(s.split('1'))-s.split('1').count(''))
else :
  result = result - (len(s.split('0'))-s.split('0').count(''))

print(result)