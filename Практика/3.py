import csv

with open('starwars.csv', newline='') as file:
    data = csv.DictReader(file)
    characters = {}
    for line in data:
        characters[line['name']] = int(line['height']) if line['height'] != 'NA' else -1

max_height = max(characters.values())
print(max_height)
for name, height in characters.items():
    if height == max_height:
        print(name)
