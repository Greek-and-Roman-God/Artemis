#1 : 1
#2 : 2
#3 : 3
#4 : 5
#5 : 8
...
#규칙을 찾아보면 피보나치 수열이라는 것을 알 수 있다

N = int(input())

first, second = 0, 1
for i in range(N) :
  first, second = second, first + second

print(second % 10007)