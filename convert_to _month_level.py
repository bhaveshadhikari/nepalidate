import json

# Load your data
with open('data/dates.json', 'r') as f:
    data = json.load(f)

# Group by year and count days per month
year_map = {}
for entry in data:
    year = entry['npYear']
    month = entry['npMonth']
    
    if year not in year_map:
        year_map[year] = {}
    
    if month not in year_map[year]:
        year_map[year][month] = 0
    
    year_map[year][month] += 1

# Convert to the format you want: year -> [days_in_month_1, days_in_month_2, ...]
result = {}
for year, months in year_map.items():
    # Sort by month number and extract day counts
    result[year] = [months[m] for m in sorted(months.keys())]

with open("map_total_month_days.json") as f:
    f.write(json.dumps(result, indent=2))