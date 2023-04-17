import sys

N = int(sys.stdin.readline())

lst = list(map(int, input().split()))

v = int(sys.stdin.readline())

sys.stdout.write(str(lst.count(v)))