import sys

K, N = map(int, input().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]

left = 1 #0으로 나누는 일이 없도록 1로 설정
right = max(lan)

result = []
while not right < left :
  cnt = 0
  mid = (left + right) // 2
  cnt += sum(i//mid for i in lan)
  
  if cnt >= N :
    result.append(mid)
    left = mid + 1
  else :
    right = mid - 1

print(max(result))