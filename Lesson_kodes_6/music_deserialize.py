import json
import pickle
with open('group.json', 'r', encoding='utf-8') as f:
    musick = json.load(f)
print(musick)
print(type(musick))
with open('group.pickle', 'rb') as f:
    musick = pickle.load(f)
print(musick)
print(type(musick))