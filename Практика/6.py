import json

with open('movies.json', encoding='utf-8') as file:
    data = json.load(file)

films = []
for film in data['docs']:
    films.append([film['name'], film['rating']['kp']])
for film in sorted(films, key=lambda f: -f[1]):
    print(film[0])