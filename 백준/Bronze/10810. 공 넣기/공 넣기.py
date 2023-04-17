N, M = map(int, input().split())

balls = [0]*N

for i in range(M):
    a, b, c = map(int, input().split())

    for j in range(a-1, b):
        balls[j] = c

for k in balls:
    print(k, end=' ')