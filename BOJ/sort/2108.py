import sys

N = int(input())

num = []
for _ in range(N) :
  num.append(int(sys.stdin.readline()))
num.sort() #오름차순으로 정렬

cnt = {} #나타나는 횟수를 저장하는 딕셔너리
for i in num :
  if i in cnt :
    cnt[i] += 1
  else :
    cnt[i] = 1

max_cnt = max(cnt.values()) #가장 많이 나타난 횟수
max_result = []
for i in cnt :
  if max_cnt == cnt[i] :
    max_result.append(i)

print(round(sum(num)/len(num))) #산술평균
print(num[len(num)//2]) #중앙값
print(max_result[1] if len(max_result) > 1 else max_result[0]) #최빈값
print(abs(num[len(num)-1] - num[0])) #범위