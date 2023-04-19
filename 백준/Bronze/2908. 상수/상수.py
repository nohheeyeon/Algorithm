A, B = input().split()

A = A[::-1]
B = B[::-1]

if A > B:
    print(A)

elif B > A:
    print(B)