import sys

T = int(sys.stdin.readline())

sum = 0

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())

    sum = A+B
    
    print(A+B)