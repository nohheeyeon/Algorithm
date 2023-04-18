count = 0
nums = []

for i in range(10):
    N = int(input())
    num = N%42

    if num not in nums:
        nums.append(num)
        count += 1

print(count)