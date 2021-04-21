N = int(input())
money = list(map(int, input().split()))
money.sort()

target = 1 #만들 수 있는지 확인할 금액

# 1 ~ X원까지 만들 수 있고 i원이 있다면,
# 1 ~ X원에 각각 i원을 더하여 1+i ~ X+i원을 만들 수 있다
for i in money :
  if target < i : #1 ~ X원과 1+i ~ X+i원의 범위에 속하지 않는 경우 (그 사이인 경우)
    break
  else :
    target += i

print(target)