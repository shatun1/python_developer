def some_f():
     return 10
result = some_f()
print(result)
#

#
a = some_f
print(a)
print(a())

# def f():
#     print("hello from orher f")
# def to(f_param):
#     f_param()
# to(f)
def n_filter(numbers, function):
    filtered_numbers = []
    for number in numbers:
        if function(number):
            filtered_numbers.append(number)
    return filtered_numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def is_even(number):
#     return number % 2 == 0

# def is_not_even(number):
#     return number % 2 != 0
#
# def big_4(number):
#     return number > 4

print(n_filter(numbers, lambda number: number % 2 == 0))
print(n_filter(numbers, lambda number: number % 2 != 0))
print(n_filter(numbers, lambda number: number > 4))
