###############################operator and
s = 'abc'
if s:
    print('Строка не пустая')
else:
    print('Строка пустая')

l = [1, 2, 3]
d = {1: 'a'}

if l and d:
    print('Список и словарь не пустые')
else:
    print('Список и словарь пустые')

import math
if 1 > 2 and math.sqrt(-1):
    print('СТОП, ты там вначале накосячил, дальше не пойду')
print('Ладно, уговорил, идем дальше')

################# operator 'or'

if 2 > 1 or math.sqrt(-1):
    print('Ошибки не будет, дальше верного условия  не иду')

numbers = [4, 1, 2, 5, 6, 8, 16]
result = [number for number in numbers if number > 0 and math.sqrt(number) < 2]
print(result)

def add_to_list(input_list=None):
    input_list = input_list or []
    input_list.append(2)
    return input_list
result = add_to_list([2, 3])
print(result)






