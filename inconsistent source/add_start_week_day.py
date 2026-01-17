import json

with open('data\dates.json', 'r') as f:
    data = json.load(f)

# Group by year and track month starts
year_map = {}
for idx, entry in enumerate(data):
    year = entry['npYear']
    month = entry['npMonth']
    day = entry['npDay']
    
    if year not in year_map:
        year_map[year] = {}
    
    if month not in year_map[year]:
        year_map[year][month] = {'days': 0, 'start_weekday': None}
    
    # Count days
    year_map[year][month]['days'] += 1
    
    # When day == 1, record the weekday (index % 7, where first entry is Saturday = 0)
    if day == 1:
        year_map[year][month]['start_weekday'] = idx % 7

# Convert to desired format
result = {}
for year, months in sorted(year_map.items()):
    result[year] = []
    for month in sorted(months.keys()):
        result[year].append([
            months[month]['days'],
            months[month]['start_weekday']
        ])

json_str = json.dumps(result, separators=(',', ':'))
# put each top-level key on its own line
json_str = json_str.replace(',"', ',\n"')

with open("map_weekdays.json", "w", encoding="utf-8") as f:
    f.write("{\n" + json_str[1:-1] + "\n}")