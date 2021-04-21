#210421
S = input()

tmp1 = 0
tmp2 = 0
#0에서 1로 뒤집는 경우와 1에서 0으로 뒤집는 경우를 나눠서 체크
for i in range(len(S)-1) :
  if S[i] == '0' and S[i+1] == '1' :
    tmp1 += 1
  elif S[i] == '1' and S[i+1] == '0' :
    tmp2 += 1

#둘 중 한 경우가 0이 아니면 최소값을 출력, 하나라도 0이 나오면 최대값을 출력
print(min(tmp1, tmp2) if not tmp1 and not tmp2 else max(tmp1, tmp2))

#201111
s = input()
zCnt = s.count('0')
oCnt = s.count('1')

result = len(s.split('1'))-s.split('1').count('') + len(s.split('0'))-s.split('0').count('')

if zCnt > oCnt :
  result = result - (len(s.split('1'))-s.split('1').count(''))
else :
  result = result - (len(s.split('0'))-s.split('0').count(''))

print(result)