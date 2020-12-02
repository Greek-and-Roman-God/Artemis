def factorial(result, N) :
  if N > 1 :
    result = N * factorial(result, N-1)
  return result

N = int(input())
print(factorial(1, N))