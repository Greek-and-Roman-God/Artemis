N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = 0
#A의 가장 작은 값과 B의 가장 큰 값을 곱해서 더해주고
#사용한 값은 리스트에서 삭제한다
for _ in range(N) :
  result += min(A) * max(B)
  A.remove(min(A))
  B.remove(max(B))
print(result)