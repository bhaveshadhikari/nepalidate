from data import TOTAL_BS_MONTHLY_DAYS, MONTH_START_WEEKDAY

# multi_dim_arr = [[None]*cols for _ in range(rows)]

calendar = [['']*7 for _ in range(6)]

def generate_calendar(year, month):
    fptr = MONTH_START_WEEKDAY[year-2000][month-1]
    
    total_days_in_month = TOTAL_BS_MONTHLY_DAYS[year-2000][month-1]
    print("total days: ", total_days_in_month)
    fill_date = 1
    
    for x in range(0, 6):
        for y in range(fptr if x == 0 else 0, 7):
            if fill_date > total_days_in_month:
                break
            calendar[x][y] = fill_date
            fill_date += 1
               

year = 2000
month = 1
# year = int(input("Year(2000-2099): "))
# month = int(input("Month: "))

if year <= 2099 and year >= 2000 and month >= 0 and month <= 11:
    generate_calendar(year, month)
else:
    print("invalid range!")
    exit()

print(" SU  MO  TU  WE  TH  FR  SA")
for row in calendar:
    for day in row:
        print(f"{day:>3}", end=" ")  # right-align in 2 spaces
    print()
