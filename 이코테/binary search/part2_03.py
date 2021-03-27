N, M = map(int, input().split())
tteok = list(map(int, input().split()))

left = 0
right = max(tteok)
H = 0
while left <= right :
  result = 0
  mid = (left + right) // 2
  result += sum(i-mid for i in tteok if i > mid) #절단기 높이보다 길이가 높은 떡만 자른다
  if result >= M : #적어도 M만큼의 떡을 얻었다면
    H = max(mid, result) #높이의 최댓값을 구한다
    left = mid + 1
  else :
    right = mid - 1

print(H)