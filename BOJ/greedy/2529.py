N = int(input())
sign = list(input().split())

nums = []
result = [] #나올 수 있는 모든 수 저장
visited = [False] * 10 #각 숫자 사용여부

def inequality(depth, pre) :

  if depth == N+1 : #수가 완성되면 string 형태로 저장
    result.append(''.join(map(str, nums)))
    return
  
  for i in range(10) :
    if sign[depth-1] == '<' and pre < i and not visited[i] : #부등호 조건을 만족하고, 사용하지 않은 숫자라면
      visited[i] = True
      nums.append(i)
      inequality(depth + 1, i)
      nums.pop()
      visited[i] = False
    elif sign[depth-1] == '>' and pre > i and not visited[i] :
      visited[i] = True
      nums.append(i)
      inequality(depth + 1, i)
      nums.pop()
      visited[i] = False

for i in range(10) :
  visited[i] = True
  nums.append(i)
  inequality(1, i)
  nums.pop()
  visited[i] = False

print(result[-1]) #최대값
print(result[0]) #최소값