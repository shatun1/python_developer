numbers = [-2, 4, -6, 2, -10, 22]
result = []
for number in numbers:
    if number > 0:
        result.append(number)
print(result)

result = filter(lambda number: number > 0, numbers)
print(list(result))

result = [number for number in numbers if number > 0]
print(result)

pairs = [(1, 'nikita'), (2, 'Sanya'), (3, 'Danya'), (4, 'Vadim')]
result = {pair[0]: pair[1] for pair in pairs}
print(result)



import random
numbers = [random.randint(1, 100) for i in range(10)]
print(numbers)


numbers = [1, 2, -7, 4]
numbers = [number**2 for number in numbers]
print(numbers)

names = ['Руслан', "Андрей", "Ангелина", "Алик", "Саша"]
names = [name for name in names if name.startswith("А")]
print(names)