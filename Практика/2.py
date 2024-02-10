import json

with open('weather.json') as file:
    data = json.load(file)

temp_min = []
temp_max = []
for w in data['list']:
    temp_min.append(w['main']['temp_min'])
    temp_max.append(w['main']['temp_max'])
print(min(temp_min))
print(max(temp_max))
