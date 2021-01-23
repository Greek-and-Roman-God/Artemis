N = int(input())
divisor = list(map(int, input().split()))
divisor.sort()
print(divisor[0] * divisor[-1]) #첫 약수와 마지막 약수를 곱하면 N을 구할 수 있다