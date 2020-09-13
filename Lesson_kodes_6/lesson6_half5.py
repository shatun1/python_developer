import json
friends = [
    {'name': 'nikita', 'age': 23, 'phone': [123, 345]},
    {'name': 'Leo', 'age': 23}
]
print(type(friends))
json_friends = json.dumps(friends)
print(json_friends)
print(type(json_friends))

friends = json.loads(json_friends)
print(friends)
print(type(friends))

friends = [
    {'name': 'nikita', 'age': 23, 'phone': [123, 345]},
    {'name': 'Leo', 'age': 23}
]

with open('friends.json', 'w') as f:
    json_friends = json.dump(friends, f)
with open('friends.json', 'r') as f:
    friends = json.load(f)
print(friends)
print(type(friends))




