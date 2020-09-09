cities = ['Las Vegas', 'Paris', 'Moscov', 'Paris', 'Moscov']
print(type(cities))
print(cities)

cities = set(cities)

print(cities)

print(type(cities))

cities = {'Las Vegas', 'Paris', 'Moscov', 'Paris', 'Moscov'}
print(cities)
cities.add('kek')
print(cities)
#cities.remove('Moscov')
print(cities)
print(len(cities ))
print('Paris' in cities)

for city in cities:
    print(city)

max_things = {'Телефон', 'бритва', 'рубашка', 'шорты'}
kate_things = {'Телефон', 'шорты', 'зонтик', 'помада'}
print(max_things | kate_things)
print(max_things & kate_things)
print(max_things - kate_things)
print(kate_things - max_things)











