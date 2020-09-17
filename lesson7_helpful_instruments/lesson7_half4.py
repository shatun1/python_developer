a = 1
b = a
b = 100
print(a)

a = [1, 2, 4]
b = a
b[1] = 100
print(a)


numbers = [1 ,2 ,3]
def change_number_in_list(input_list):
    input_list[1] = 200
change_number_in_list(numbers)
print(numbers)
a = [1, 2, 3]
b = a[:]
b[1] = 200
print(a)


b = a.copy()
b[1] = 200
print(a)
import copy
a = [1, 2, [3, 4]]
b = copy.deepcopy(a)
b[2][1] = 145
print(a)
print(b)
