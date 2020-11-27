A, B = input().split()
A = int(A[2] + A[1] + A[0])
B = int(B[2] + B[1] + B[0])

print(A if A > B else B)