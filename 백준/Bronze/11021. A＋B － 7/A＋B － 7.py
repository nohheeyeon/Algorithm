import sys

T = int(sys.stdin.readline())

A = 0
B = 0

for i in range(1, T+1):
    A, B = map(int, sys.stdin.readline().split())

    sum = A+B

    sys.stdout.write("Case #{}: {} \n".format(i, sum))