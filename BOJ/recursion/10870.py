#처음 생각한 풀이법
def fibonacci(first, second, n, temp) :
  if n <= 1 :
    print(n)
    return
  elif temp < n :
    temp += 1
    first, second = second, first + second
    fibonacci(first, second, n, temp)
  else :
    print(second)

n = int(input())
fibonacci(0,1,n,1)

"""
#더 간단한 풀이법
def fibonacci(n) :
  if n <= 1 :
    return num
  return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(fibonacci(n))
"""