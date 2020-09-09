# def information(name, age):
#     information1 = f'{name}, {age} года(лет), проживает в городе Ессентуки'
#     return  information1
# name = input("Введите имя")
# age = input('Введите возраст')
# print(information(name, age))
#
def max_number(a, b, c):
    result = max([a, b ,c])
    return result
print(max_number(2, 4, 6))


player = {'name': input("Введите имя игрока"), 'health': 100, 'damage': 25, 'armor': 1.2}
enemy = {'name': input('Введите имя противника'), 'health': 100, 'damage': 25, 'armor': 1.2}
print('До атаки')
print(enemy)
print(player)

def damage_armor(damage, armor):
    return damage / armor


def atack(unit, target):
    damage = damage_armor(unit['damage'], target['armor'])
    target['health'] -= damage
atack(player, enemy)
print('После атаки')




