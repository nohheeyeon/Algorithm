N, M = map(int, input().split())
baskets = list(range(1, N+1))

for j in range(M):
    a,b = map(int, input().split())

    baskets[a-1 : b] = reversed(baskets[a-1 : b])

print(*baskets)