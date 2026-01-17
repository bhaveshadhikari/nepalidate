from data import TOTAL_BS_MONTHLY_DAYS, MONTH_START_WEEKDAY


def generate_calendar(year, month):
    """Generate calendar grid for given BS year and month."""
    if not (2000 <= year <= 2099 and 1 <= month <= 12):
        raise ValueError(f"Invalid year {year} or month {month}")
    
    grid = [[''] * 7 for _ in range(6)]
    
    year_idx = year - 2000
    month_idx = month - 1
    
    start_day = MONTH_START_WEEKDAY[year_idx][month_idx]
    total_days = TOTAL_BS_MONTHLY_DAYS[year_idx][month_idx]
    
    day = 1
    for row in range(6):
        start_col = start_day if row == 0 else 0
        for col in range(start_col, 7):
            if day > total_days:
                return grid
            grid[row][col] = day
            day += 1
    
    return grid


def print_calendar(grid):
    print("")
    print("----------------------------")
    print(" SU  MO  TU  WE  TH  FR  SA")
    print("----------------------------")
    for row in grid:
        if all(x == '' for x in row): # skip empty row
            break
        for day in row:
            print(f"{day:>3}", end=" ")  # right-align in 2 spaces
        print()
    print("----------------------------")

if __name__ == "__main__":
    try:
        year = int(input("Year (2000-2099): "))
        month = int(input("Month (1-12): "))
        
        grid = generate_calendar(year, month)
        print_calendar(grid)
        
    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nCancelled.")