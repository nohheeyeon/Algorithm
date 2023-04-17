import sys

T = int(sys.stdin.readline())

for i in range(1, T+1):
    A, B = map(int, sys.stdin.readline().split())

    sum = A+B

    sys.stdout.write("Case #{}: {} + {} = {} \n".format(i, A, B, sum))