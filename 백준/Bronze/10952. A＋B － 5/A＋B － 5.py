import sys

while True:

    A, B = map(int, sys.stdin.readline().split())
    
    if A == 0 and B == 0:

        break

    if 0 < A < 10 and 0 < B < 10:

     sys.stdout.write(str(A+B) + "\n")