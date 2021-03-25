N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort() #오름차순 정렬
B.sort(reverse=True) #내림차순 정렬
for i in range(K) :
  if A[i] < B[i] : #A의 원소가 작으면 바꾼다
    A[i], B[i] = B[i], A[i]

print(sum(A))