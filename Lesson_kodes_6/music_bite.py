import pickle
import json
my_favourite_group = {
'name': 'Г.М.О.',
"tracks": ['Последний месяц осени', 'Шапито'],
'Albums': [{'name': 'Делать панк-рок','year': 2016},
{'name': 'Шапито','year': 2014}]}
j_grop = json.dumps(my_favourite_group)
print(j_grop)
print(type(j_grop))
p_group = pickle.dumps(my_favourite_group)
print(p_group)
print(type(p_group))

with open('group.pickle', 'wb') as f:
    pickle_group = pickle.dump(my_favourite_group, f)
print(pickle_group)

with open('group.json', 'w', encoding='utf-8') as f:
    json_grop = json.dump(my_favourite_group, f)
print(json_grop)





