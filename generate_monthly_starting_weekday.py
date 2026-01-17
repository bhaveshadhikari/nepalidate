from data import TOTAL_BS_MONTHLY_DAYS

#initial: 2000-01-01, Wed

start_weekdays = [[None]*12 for _ in range(100)]

start_weekday = 3 # sun:0 - sat(6)

for x in range(0,100):
    for y in range(0, 12):
        start_weekdays[x][y] = start_weekday
        total_days_in_current_month = TOTAL_BS_MONTHLY_DAYS[x][y]
        start_weekday += total_days_in_current_month
        # print(f"before: {start_weekdays[x][y]}, after: {start_weekday}")
        start_weekday %= 7
        
start_weekdays_metadata_str = f"{start_weekdays}".replace(', [', ',\n[')
print("[\n" + start_weekdays_metadata_str[1:-1] + "\n]")
# print(start_weekdays)


