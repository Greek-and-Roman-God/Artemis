N = int(input())

cnt = 0
arr = [0 for _ in range(1000001)]
arr[2], arr[3] = 1, 1 #활용할 값을 미리 할당해준다
for i in range(4, N+1) :
  #2로 나누는 것, 3으로 나누는 것, 1을 빼는 것 중
  #가장 최소값 + 1을 해당 인덱스에 할당해준다
  #이 때, 이전의 값을 활용한다
  arr[i] = min(arr[i//2] if not i % 2 else 1000000, arr[i//3] if not i % 3 else 1000000, arr[i-1]) + 1

print(arr[N])