import math
Fructs_list1 = ['Апельсины', "Мандарины",'Яблоки', "Груши"]
Fructs_list2 = ["Апельсины", 'Виноград', "Малина", "Груши",]
result = [i for i in Fructs_list1 for j in Fructs_list2 if i == j]
print(result)
numbers = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 27]
result = [number for number in numbers if number > 0 and number % 3 == 0 and number % 4 !=0]
print(result)
numbers = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 27]


def number_sqrt(numbers):
    result = []
    result = [number if number < 0 else number**2 for number in numbers]
    return result
print(number_sqrt(numbers))
print(numbers)

num = int(input('Введите число от 1 до 100'))
def function(num):
    if num == 13:
        raise ValueError('Я не могу определить это число')
    else:
        return num**2
print(function(num))
try:
    function(num)
except ValueError as e:
    print('Попробуйте ввести другое число')
    print('Информация об исключенеии', ':', e)

#function(num)

