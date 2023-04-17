N, M = map(int, input().split())

baskets = list(range(1, N+1))

for i in range(M):
    a, b = map(int, input().split())

    baskets[a-1], baskets[b-1] = baskets[b-1], baskets[a-1]

print(*baskets)