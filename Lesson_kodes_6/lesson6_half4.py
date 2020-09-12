# person = {'name': 'Max', 'phones': [123, 345]}
#
# with open('person.dat', 'wb') as f:
#     name = person['name']
#     f.write(f'{name}\n'.encode('utf-8'))
#
#     phones = person['phones']
#     for phone in phones:
#         f.write(f'{phone}\n'.encode('utf-8'))
# print('Object has written')

# with open('person.dat', 'rb') as f:
#     result = f.readlines()
#
# person = {}
#
# person['name'] = result[0].decode("utf-8").replace('\n', '')
#
# phones = []
# for bphone in result[1:]:
#     phones.append(bphone.decode('utf-8').replace('\n', ''))
#
# person['phones'] = phones
# print(person)

# Правильный способ записи и чтения >>>>>>>>>>>>>>>

import pickle

# person = {'name': 'Max', 'phones': [123, 345]}
# with open('person.dat', 'wb') as f:
#     pickle.dump(person, f)
# print("Object has written")

with open('person.dat', 'rb') as f:
    person = pickle.load(f)
print(person)












