#cmp_to_key 사용
from functools import cmp_to_key

K, N =  map(int, input().split())
num = [int(input()) for _ in range(K)]

max_num = max(num)
for i in range(N-K) :
  num.append(max_num) #제일 큰 수를 중복 이용할 것

#숫자 위치를 바꿔보면서 큰 것을 앞으로 정렬
num = sorted(num, key=cmp_to_key(lambda a, b : -1 if int(str(a)+str(b)) > int(str(b)+str(a)) else 1))
print("".join(map(str, num)))



##########################
#정렬 실패
K, N =  map(int, input().split())
num = [int(input()) for _ in range(K)]

max_num = max(num)
for i in range(N-K) :
  num.append(max_num)

num = list(map(str, num))
num = sorted(num, key=lambda num : num[0], reverse=True)

print("".join(map(str, num)))

###########################
#permutations 이용, 시간초과
from itertools import permutations

K, N =  map(int, input().split())
num = [int(input()) for _ in range(K)]

max_num = max(num)
for i in range(N-K) :
  num.append(max_num)

result = 0
for i in permutations(num, N) :
  result = max(result, int("".join(map(str, i))))

print(result)