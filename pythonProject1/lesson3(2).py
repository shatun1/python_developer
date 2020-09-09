empity_list = []
friends = ['Max', 'Leo', 'Kate']
print(type(friends))
print("Первый друг", friends[0])
print("last friend", friends[-1])

print(friends)
print(len(friends))
friends.append(('Ron'))
print(friends)
print(len(friends))
print(friends.pop())
friends.clear()
print(friends)
friends = ['Max', 'Leo', 'Kate']
friends.remove('Kate')
print(friends)
del friends[0]
print(friends)
#"Max" in friends

hero = 'halk'
if hero.find('man') != -1:
    print('Есть')
else: print('not')

if 'ha' in hero:
    print('Есть')
else:print('not')

goals = ['Стать гуру языка python', "здоровье", "я хачу питцы"]
if "я хачу питцы" in goals:
    print("Молодец, ты ничего не забыл")
else:print('not')

print("Соревнования по Python")
competitors = int(input("Введите кол-во участников"))
i = competitors
members = []
while i > 0:
    name = input('Кто занял {} место'.format(i))
    members.append(name)
    i -= 1
print("В соревновании участвовали", sorted(members))
members.reverse()
result = members[:3]
result = "Победители: {}. Поздравляем".format(result)
print(result)











