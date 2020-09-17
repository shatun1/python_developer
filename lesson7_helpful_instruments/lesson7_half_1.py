is_has_name = True
name = 'Max' if is_has_name else 'Empity'
print(name)

is_one = False
number = 1 if is_one else 2
print(number)

word = 'Hello'
result = []

for i in range(len(word)):
    letter = word[i]
    letter = letter.lower() if i%2 == 0 else letter.upper()
    result.append(letter)
result = ''.join(result)
print(result)

password = input('Введите пароль')
print('Войти' if password == 'secret' else 'отказано в доступе')


















