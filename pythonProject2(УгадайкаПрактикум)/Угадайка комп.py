import random
user_number = int(input("Введи число, которое должен угадать компьютер: "))
count = 0

numbers_massive = []
i = 0
for number in range(0, 100):
    if i <= 100:
        numbers_massive.append(number)
        i += 1
print(numbers_massive)

min_number = 0
max_number = 100
while True:
    count += 1
    n = random.randint(min_number, max_number)
    if numbers_massive[n] == user_number:
        print(f"Правильное число было: {user_number}, вы победили с {count} попытки.")
        break
    elif numbers_massive[n] < user_number:
        print(f"Число{[n]} слишком маленькое")
        min_number = 0
    else:
        print(f"Число{[n]} слишком большое")
        max_number = n - 1
