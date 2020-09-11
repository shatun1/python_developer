# import math
from random import choice, sample, shuffle
# r = 100
# print(2*r*math.pi)
#
# print((r**2)*math.pi) #квадрат числа
# print((math.pow(r, 2))*math.pi)
#
#
# x1=10
# y1=10
# x2=50
# y2=100
# l=math.sqrt((x1-x2)**1+(y1-y2)**2) #корень числа
#
# print(math.factorial(5))
players = ['Nik', 'Sanya', 'Danya', 'Ilya', 'Vadim']
print(choice(players))
print(sample(players, 3))

cards = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
print(cards)
shuffle(cards)
print(cards)






