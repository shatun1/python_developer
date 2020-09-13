import json

favorite_tracks = [
    {'name': 'Godzilla', 'artist': 'Eminem'},
    {'name': 'hex', 'artist': 'no_singer'}
]

with open('tracks.json', 'w', encoding='utf-8') as f:
    json.dump(favorite_tracks, f)
print('get')
# with open('tracks.json', 'r', encoding='utf-8') as f:
#      musick = json.load(f)
# print(musick)