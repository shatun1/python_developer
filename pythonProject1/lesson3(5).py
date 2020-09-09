friends = ['Max', 'Leo', 'Kate']
friend = {
    'name': "Sanya",
    'age': 23
}
print((friend))
print(type(friend))

print(friend['age'])
friend['has car'] = False
print(friend)
# del friend['age']
print(friend)
if 'age' in friend:
     print('Есть возраст')
else:print('Ты что то забыл')
if 'has car' in friend:
    print('Есть машина')

for val in friend.values():
    print(val)
for item in friend.items():
    print((item))

for key, val in friend.items(): 
    print(key)
    print(val)
