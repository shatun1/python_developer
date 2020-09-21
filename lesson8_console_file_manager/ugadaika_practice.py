import random
def ugadaika_game():
    number = random.randint(1, 100)
    #print(number)
    user_number = None
    count = 0
    levels = {1: 10, 2: 6, 3: 4}
    try:
        level = int(input("Input your level of difficult(from 1 to 3): "))
    except KeyError:
        print('Введте положительный уровень сложности от 1 до 3')
    try:
        user_count = int(input("Введите количество пользователей: "))
    except KeyError:
        print('Введите положительное количество пользователей')
    users = []

    for i in range(user_count):
        user_name = input(f'enter user name {i}: ')
        users.append(user_name)
    print(users)


    max_count = levels[level]
    is_winner = False
    winner_name = None

    while not is_winner:
        count+=1
        if count > max_count:
            print("All users are loosers")
            break

        print(f'try № {count} ')

        for user in users:
            print(f"Ход пользователя: {user}")

            user_number = int(input('Введите число :'))

            if user_number == number:
                is_winner = True
                winner_name = user
                break
            elif number < user_number:
                print("Ваше число больше загаданного!")
            else:
                print("Ваше число меньше загаданного!")
    else:print(f"Winer: {winner_name}")






















