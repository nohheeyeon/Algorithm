N = int(input())
score = list(map(int,input().split()))
M = max(score)

scores = 0

for i in range(N):
    score[i] = score[i]/M*100
    scores += score[i]

print(scores/N)