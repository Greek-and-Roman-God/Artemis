N = int(input())
rope = [int(input()) for _ in range(N)]

rope.sort() #로프를 들 수 있는 중량 순으로 정렬
w = 0
for i in range(1, N+1) :
  w = max(w, rope[-i] * i) #제일 많이 들 수 있는 로프 i개를 뽑아 그 중에서 가장 적은 중량 * i를 구함

print(w)