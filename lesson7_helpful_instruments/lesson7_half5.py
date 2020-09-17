# number = int(input('Введите число'))
# try:
#     result = 100 / number
# except ZeroDivisionError as e:
#     print('Деление на 0')
#     print('Информация об исключенеии', ':', e)
# except Exception as e:
#     print('Неизвестная ошибка')
#     print('Информация об исключенеии', ':', e)
# print('Конец')

number = int(input('Введите число'))
try:
    result = 100 / number
except:
    print('Деление на ноль')
else:
    print('Всё хорошо, ошибок не было')
finally:
    print('Что делаем, когда ошибка есть или её нет')

print('begining')
raise Exception('Что то пошло не так')
print('Finish')