import random
min_number = 1
max_number = 100
user_unsver = None
while user_unsver != '=':
    r_number = random.randint(min_number, max_number)
    print(r_number)
    user_unsver = input('< > =')
    if user_unsver == '<':
        print("Число слишком маленькое")
        min_number = r_number + 1
    if user_unsver == '>':
        print("Число слишком большое")
        max_number = r_number - 1
print("Вы победили")
