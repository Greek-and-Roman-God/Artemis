N, K = map(int, input().split())

money = []
for _ in range(N) :
  money.append(int(input()))
money.reverse() #내림차순으로 정렬

cnt = 0
for i in money :
  if K // i > 0 : #나눠지면 (1개라도 지불할 수 있으면)
    cnt += K // i
    K = K % i #남은 돈을 업데이트

print(cnt)