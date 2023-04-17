students = set(range(1, 31))
numbers = set()

for i in range(28):
    num = int(input())
    numbers.add(num)

    missing = sorted(students - numbers)

print(missing[0], missing[1], sep='\n')