import csv
import json

with open('rate.json', encoding='utf-8') as file:
    data = json.load(file)

rates = []
for _, value in data['Valute'].items():
    rates.append([value['CharCode'], value['Name']])

rates.sort(key=lambda x: x[0])

with open('result.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['CharCode', 'Name'])
    writer.writerows(rates)
