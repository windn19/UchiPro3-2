import csv

with open('ratings.csv', newline='') as file:
    data = csv.DictReader(file)
    films = []
    for line in data:
        if 'drama' in line['Genres']:
            films.append(line['Title'])

print(len(films))
